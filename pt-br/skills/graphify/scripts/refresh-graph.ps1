# Reconstrói o índice Graphify local quando o código muda e verifica o resultado.
# Uso: pwsh ./refresh-graph.ps1 [-CheckOnly] [-Force]   (PowerShell 7+, qualquer sistema)
[CmdletBinding()]
param(
    [switch] $CheckOnly,
    [switch] $Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = (& git rev-parse --show-toplevel 2>$null).Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($repoRoot)) {
    throw 'Execute este script de dentro de um repositório Git.'
}

$repoRoot = [IO.Path]::GetFullPath($repoRoot)
$outputDirectory = [IO.Path]::GetFullPath((Join-Path $repoRoot 'graphify-out'))
$expectedOutputDirectory = [IO.Path]::GetFullPath((Join-Path $repoRoot 'graphify-out'))
if ($outputDirectory -ne $expectedOutputDirectory -or
    -not $outputDirectory.StartsWith(
        $repoRoot + [IO.Path]::DirectorySeparatorChar,
        [StringComparison]::OrdinalIgnoreCase)) {
    throw "Caminho inesperado para a saída do Graphify; operação recusada: $outputDirectory"
}

$graphPath = Join-Path $outputDirectory 'graph.json'
$manifestPath = Join-Path $outputDirectory 'manifest.json'
$supportedExtensions = [Collections.Generic.HashSet[string]]::new(
    [StringComparer]::OrdinalIgnoreCase)
@(
    '.ps1', '.psm1', '.psd1', '.sh', '.bash',
    '.sln', '.slnx', '.csproj', '.fsproj', '.vbproj', '.cs', '.razor', '.cshtml', '.xaml',
    '.ts', '.tsx', '.mts', '.cts', '.js', '.jsx', '.mjs', '.json',
    '.vue', '.svelte', '.astro', '.sql',
    '.py', '.go', '.rs', '.java', '.kt', '.kts', '.scala', '.php', '.rb',
    '.c', '.h', '.cpp', '.cc', '.cxx', '.hpp', '.swift', '.dart'
) | ForEach-Object { [void] $supportedExtensions.Add($_) }

# Caminhos que o grafo nunca indexa. Ajuste-os ao repositório e mantenha .graphifyignore sincronizado.
# Um prefixo terminado em '/' corresponde a essa pasta na raiz e em qualquer nível.
$excludedFolders = @('.claude/', '.agents/', '.codex/', '.cursor/', '.opencode/', '.git/', 'graphify-out/', 'node_modules/', 'dist/', 'build/', 'bin/', 'obj/')
$excludedFileSuffixes = @('package-lock.json')

function Test-Excluded([string] $normalized) {
    foreach ($folder in $excludedFolders) {
        if ($normalized.StartsWith($folder, [StringComparison]::OrdinalIgnoreCase) -or
            $normalized.Contains('/' + $folder, [StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }
    }
    foreach ($suffix in $excludedFileSuffixes) {
        if ($normalized.EndsWith($suffix, [StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }
    }
    return $false
}

function Get-CurrentCodeFiles {
    $paths = @(& git -C $repoRoot ls-files --cached --others --exclude-standard)
    if ($LASTEXITCODE -ne 0) {
        throw 'Não foi possível enumerar os arquivos do repositório.'
    }

    foreach ($relativePath in $paths) {
        $normalized = $relativePath.Replace('\', '/')
        # Deve permanecer sincronizado com .graphifyignore: se um caminho for indexado por uma lista
        # e enumerado pela outra, a verificação de atualidade ficará sempre desatualizada.
        if (Test-Excluded $normalized) {
            continue
        }

        if (-not $supportedExtensions.Contains([IO.Path]::GetExtension($normalized))) {
            continue
        }

        $fullPath = [IO.Path]::GetFullPath((Join-Path $repoRoot $relativePath))
        if (Test-Path -LiteralPath $fullPath -PathType Leaf) {
            [pscustomobject]@{ RelativePath = $normalized; FullPath = $fullPath }
        }
    }
}

function Get-GraphFreshness {
    if (-not (Test-Path -LiteralPath $graphPath -PathType Leaf) -or
        -not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
        return [pscustomobject]@{ Fresh = $false; Reason = 'o grafo ou o manifesto não existe'; Files = 0 }
    }

    $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    $manifestEntries = @($manifest.PSObject.Properties)
    $graph = Get-Content -LiteralPath $graphPath -Raw | ConvertFrom-Json
    if ($graph.nodes | Where-Object {
        $_.source_file -and [IO.Path]::GetExtension([string] $_.source_file) -eq '.md'
    } | Select-Object -First 1) {
        return [pscustomobject]@{ Fresh = $false; Reason = 'o grafo contém nós Markdown de uma atualização incremental insegura'; Files = 0 }
    }

    $codeManifestEntries = @($manifestEntries | Where-Object {
        $supportedExtensions.Contains([IO.Path]::GetExtension($_.Name))
    })

    $manifestPaths = [Collections.Generic.HashSet[string]]::new(
        [StringComparer]::OrdinalIgnoreCase)
    foreach ($entry in $codeManifestEntries) {
        $relativePath = $entry.Name.Replace('\', '/')
        [void] $manifestPaths.Add($relativePath)
        $fullPath = [IO.Path]::GetFullPath((Join-Path $repoRoot $relativePath))
        if (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
            return [pscustomobject]@{ Fresh = $false; Reason = "arquivo indexado foi removido: $relativePath"; Files = $codeManifestEntries.Count }
        }

        $expectedHash = [string] $entry.Value.ast_hash
        $actualHash = (Get-FileHash -LiteralPath $fullPath -Algorithm MD5).Hash.ToLowerInvariant()
        if ($actualHash -ne $expectedHash.ToLowerInvariant()) {
            return [pscustomobject]@{ Fresh = $false; Reason = "o código-fonte mudou: $relativePath"; Files = $codeManifestEntries.Count }
        }
    }

    $currentFiles = @(Get-CurrentCodeFiles)
    foreach ($file in $currentFiles) {
        if (-not $manifestPaths.Contains($file.RelativePath)) {
            return [pscustomobject]@{ Fresh = $false; Reason = "novo arquivo de código-fonte: $($file.RelativePath)"; Files = $codeManifestEntries.Count }
        }
    }

    return [pscustomobject]@{ Fresh = $true; Reason = 'os hashes do código-fonte correspondem ao manifesto somente de código'; Files = $codeManifestEntries.Count }
}

$freshness = Get-GraphFreshness
if ($CheckOnly) {
    $state = if ($freshness.Fresh) { 'fresh' } else { 'stale' }
    $translatedState = if ($freshness.Fresh) { 'atualizado' } else { 'desatualizado' }
    Write-Output "Índice do Graphify ${translatedState}: $($freshness.Reason) ($($freshness.Files) arquivos indexados)."
    if (-not $freshness.Fresh) { exit 2 }
    exit 0
}

if ($freshness.Fresh -and -not $Force) {
    Write-Output "Índice do Graphify atualizado ($($freshness.Files) arquivos indexados); reconstrução ignorada."
    exit 0
}

$trackedOutput = @(& git -C $repoRoot ls-files -- graphify-out)
if ($trackedOutput.Count -gt 0) {
    throw 'Recusa em substituir graphify-out porque contém arquivos rastreados pelo Git.'
}

& git -C $repoRoot check-ignore -q -- graphify-out/graph.json
if ($LASTEXITCODE -ne 0) {
    throw 'Recusa em reconstruir até que graphify-out/ seja ignorado pelo Git.'
}

if (Test-Path -LiteralPath $outputDirectory) {
    Remove-Item -LiteralPath $outputDirectory -Recurse -Force
}

Push-Location $repoRoot
try {
    & graphify extract . --code-only --timing
    if ($LASTEXITCODE -ne 0) {
        throw "A extração do Graphify falhou com o código de saída $LASTEXITCODE."
    }

    & graphify diagnose multigraph --graph $graphPath --max-examples 3
    if ($LASTEXITCODE -ne 0) {
        throw "O diagnóstico de integridade do Graphify falhou com o código de saída $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

$freshness = Get-GraphFreshness
if (-not $freshness.Fresh) {
    throw "O Graphify foi reconstruído, mas o manifesto continua desatualizado: $($freshness.Reason)"
}

Write-Output "Índice do Graphify reconstruído e verificado ($($freshness.Files) arquivos indexados)."
