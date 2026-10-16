# Rebuilds the local Graphify index when source changed, and verifies it.
# Usage: pwsh ./refresh-graph.ps1 [-CheckOnly] [-Force]   (PowerShell 7+, any OS)
[CmdletBinding()]
param(
    [switch] $CheckOnly,
    [switch] $Force
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$repoRoot = (& git rev-parse --show-toplevel 2>$null).Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($repoRoot)) {
    throw 'Run this script from inside a Git repository.'
}

$repoRoot = [IO.Path]::GetFullPath($repoRoot)
$outputDirectory = [IO.Path]::GetFullPath((Join-Path $repoRoot 'graphify-out'))
$expectedOutputDirectory = [IO.Path]::GetFullPath((Join-Path $repoRoot 'graphify-out'))
if ($outputDirectory -ne $expectedOutputDirectory -or
    -not $outputDirectory.StartsWith(
        $repoRoot + [IO.Path]::DirectorySeparatorChar,
        [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing unexpected Graphify output path: $outputDirectory"
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

# Paths the graph never indexes. Adjust to the repository, and keep .graphifyignore in step.
# A prefix ending in '/' matches that folder at the root and at any depth.
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
        throw 'Could not enumerate repository files.'
    }

    foreach ($relativePath in $paths) {
        $normalized = $relativePath.Replace('\', '/')
        # Must stay in step with .graphifyignore: a path indexed by one and enumerated by
        # the other makes the freshness check permanently stale.
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
        return [pscustomobject]@{ Fresh = $false; Reason = 'graph or manifest is missing'; Files = 0 }
    }

    $manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
    $manifestEntries = @($manifest.PSObject.Properties)
    $graph = Get-Content -LiteralPath $graphPath -Raw | ConvertFrom-Json
    if ($graph.nodes | Where-Object {
        $_.source_file -and [IO.Path]::GetExtension([string] $_.source_file) -eq '.md'
    } | Select-Object -First 1) {
        return [pscustomobject]@{ Fresh = $false; Reason = 'graph contains Markdown nodes from an unsafe incremental update'; Files = 0 }
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
            return [pscustomobject]@{ Fresh = $false; Reason = "indexed file was removed: $relativePath"; Files = $codeManifestEntries.Count }
        }

        $expectedHash = [string] $entry.Value.ast_hash
        $actualHash = (Get-FileHash -LiteralPath $fullPath -Algorithm MD5).Hash.ToLowerInvariant()
        if ($actualHash -ne $expectedHash.ToLowerInvariant()) {
            return [pscustomobject]@{ Fresh = $false; Reason = "source changed: $relativePath"; Files = $codeManifestEntries.Count }
        }
    }

    $currentFiles = @(Get-CurrentCodeFiles)
    foreach ($file in $currentFiles) {
        if (-not $manifestPaths.Contains($file.RelativePath)) {
            return [pscustomobject]@{ Fresh = $false; Reason = "new source file: $($file.RelativePath)"; Files = $codeManifestEntries.Count }
        }
    }

    return [pscustomobject]@{ Fresh = $true; Reason = 'source hashes match the code-only manifest'; Files = $codeManifestEntries.Count }
}

$freshness = Get-GraphFreshness
if ($CheckOnly) {
    $state = if ($freshness.Fresh) { 'fresh' } else { 'stale' }
    Write-Output "Graphify index is ${state}: $($freshness.Reason) ($($freshness.Files) indexed files)."
    if (-not $freshness.Fresh) { exit 2 }
    exit 0
}

if ($freshness.Fresh -and -not $Force) {
    Write-Output "Graphify index is fresh ($($freshness.Files) indexed files); rebuild skipped."
    exit 0
}

$trackedOutput = @(& git -C $repoRoot ls-files -- graphify-out)
if ($trackedOutput.Count -gt 0) {
    throw 'Refusing to replace graphify-out because it contains tracked files.'
}

& git -C $repoRoot check-ignore -q -- graphify-out/graph.json
if ($LASTEXITCODE -ne 0) {
    throw 'Refusing to rebuild until graphify-out/ is ignored by Git.'
}

if (Test-Path -LiteralPath $outputDirectory) {
    Remove-Item -LiteralPath $outputDirectory -Recurse -Force
}

Push-Location $repoRoot
try {
    & graphify extract . --code-only --timing
    if ($LASTEXITCODE -ne 0) {
        throw "Graphify extraction failed with exit code $LASTEXITCODE."
    }

    & graphify diagnose multigraph --graph $graphPath --max-examples 3
    if ($LASTEXITCODE -ne 0) {
        throw "Graphify integrity diagnostic failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

$freshness = Get-GraphFreshness
if (-not $freshness.Fresh) {
    throw "Graphify rebuilt, but its manifest is still stale: $($freshness.Reason)"
}

Write-Output "Graphify index rebuilt and verified ($($freshness.Files) indexed files)."
