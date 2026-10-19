# Verificação somente leitura de prontidão do Graphify para hooks de início de sessão do Claude Code e Cursor.
# Requer PowerShell 7+ e Git. Não instala ferramentas, grava arquivos, acessa a rede
# nem reconstrói o índice do Graphify.
[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateSet('claude', 'cursor')]
    [string] $Harness
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-HookContext([string] $Message) {
    if ([string]::IsNullOrWhiteSpace($Message)) { return }

    if ($Harness -eq 'claude') {
        @{ hookSpecificOutput = @{ hookEventName = 'SessionStart'; additionalContext = $Message } } |
            ConvertTo-Json -Depth 5 -Compress
    }
    else {
        @{ additional_context = $Message } | ConvertTo-Json -Depth 5 -Compress
    }
}

$gitCommand = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCommand) {
    if ((Test-Path -LiteralPath (Join-Path (Get-Location) '.graphifyignore') -PathType Leaf) -or
        (Test-Path -LiteralPath (Join-Path (Get-Location) 'graphify-out') -PathType Container)) {
        Write-HookContext 'Verificação de prontidão do Graphify ignorada: Git não está disponível. Instale o Git e use a skill configuração do Graphify para verificar este projeto.'
    }
    exit 0
}

$repoRootOutput = & git rev-parse --show-toplevel 2>$null
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace(($repoRootOutput -join ''))) {
    # This hook may be installed in a non-Git workspace. It should not make that session fail.
    exit 0
}
$repoRoot = [IO.Path]::GetFullPath(($repoRootOutput -join '').Trim())

$cli = Get-Command graphify -ErrorAction SilentlyContinue
$refreshCandidates = @(
    (Join-Path $repoRoot '.agents/skills/graphify/scripts/refresh-graph.ps1'),
    (Join-Path $repoRoot '.claude/skills/graphify/scripts/refresh-graph.ps1'),
    (Join-Path $repoRoot '.cursor/skills/graphify/scripts/refresh-graph.ps1')
)
$refreshScript = $refreshCandidates | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } | Select-Object -First 1
$refreshScriptFound = -not [string]::IsNullOrWhiteSpace([string] $refreshScript)
$ignorePath = Join-Path $repoRoot '.graphifyignore'
$graphDirectory = Join-Path $repoRoot 'graphify-out'
$dependenciesPath = Join-Path $repoRoot 'docs/acordos/dependencias.md'

# Only report when the repository signals that Graphify is intended. This keeps an optional
# hook silent in repositories that do not use Graphify.
$graphifyDeclared = (Test-Path -LiteralPath $ignorePath -PathType Leaf) -or
    (Test-Path -LiteralPath $graphDirectory -PathType Container) -or
    $refreshScriptFound -or
    ((Test-Path -LiteralPath $dependenciesPath -PathType Leaf) -and
        (Select-String -LiteralPath $dependenciesPath -Pattern 'Graphify|graphifyy' -Quiet))
if (-not $graphifyDeclared) { exit 0 }

$issues = [Collections.Generic.List[string]]::new()
if (-not $cli) { $issues.Add('o CLI graphify não está no PATH') }
if (-not (Test-Path -LiteralPath $ignorePath -PathType Leaf)) { $issues.Add('o .graphifyignore da raiz não existe') }
if (-not $refreshScriptFound) { $issues.Add('a skill de navegação Graphify e o script de atualização não estão na pasta de skills do projeto') }
& git -C $repoRoot check-ignore -q -- graphify-out/graph.json
if ($LASTEXITCODE -ne 0) {
    $issues.Add('o .gitignore da raiz não ignora graphify-out/')
}

if ($issues.Count -gt 0) {
    $issueText = $issues -join '; '
    Write-HookContext "A configuração do Graphify está incompleta: $issueText. Use a skill configuração do Graphify para revisar e corrigir. Este hook não alterou nada."
    exit 0
}

$checkOutput = & pwsh -NoLogo -NoProfile -File $refreshScript -CheckOnly 2>&1
$checkExitCode = $LASTEXITCODE
if ($checkExitCode -eq 0) { exit 0 }

$detail = ($checkOutput | ForEach-Object { $_.ToString().Trim() } | Where-Object { $_ }) -join ' '
if ([string]::IsNullOrWhiteSpace($detail)) { $detail = 'o índice não existe ou está desatualizado' }
Write-HookContext "O Graphify está configurado, mas o índice não está pronto ($detail). Atualize-o com a skill graphify antes de consultar o grafo."
exit 0
