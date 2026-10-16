# Read-only Graphify readiness check for Claude Code and Cursor session-start hooks.
# Requires PowerShell 7+ and Git. It never installs tools, writes files, uses the network,
# or rebuilds the Graphify index.
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
        Write-HookContext 'Graphify readiness check skipped: Git is not available. Install Git, then use the graphify-setup skill to check this project.'
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
$dependenciesPath = Join-Path $repoRoot 'docs/agreements/dependencies.md'

# Only report when the repository signals that Graphify is intended. This keeps an optional
# hook silent in repositories that do not use Graphify.
$graphifyDeclared = (Test-Path -LiteralPath $ignorePath -PathType Leaf) -or
    (Test-Path -LiteralPath $graphDirectory -PathType Container) -or
    $refreshScriptFound -or
    ((Test-Path -LiteralPath $dependenciesPath -PathType Leaf) -and
        (Select-String -LiteralPath $dependenciesPath -Pattern 'Graphify|graphifyy' -Quiet))
if (-not $graphifyDeclared) { exit 0 }

$issues = [Collections.Generic.List[string]]::new()
if (-not $cli) { $issues.Add('the graphify CLI is not on PATH') }
if (-not (Test-Path -LiteralPath $ignorePath -PathType Leaf)) { $issues.Add('the root .graphifyignore is missing') }
if (-not $refreshScriptFound) { $issues.Add('the Graphify navigation skill and refresh script are missing from the project skill folder') }
& git -C $repoRoot check-ignore -q -- graphify-out/graph.json
if ($LASTEXITCODE -ne 0) {
    $issues.Add('the root .gitignore does not ignore graphify-out/')
}

if ($issues.Count -gt 0) {
    $issueText = $issues -join '; '
    Write-HookContext "Graphify setup is incomplete: $issueText. Use the graphify-setup skill to review and repair it. This hook did not change anything."
    exit 0
}

$checkOutput = & pwsh -NoLogo -NoProfile -File $refreshScript -CheckOnly 2>&1
$checkExitCode = $LASTEXITCODE
if ($checkExitCode -eq 0) { exit 0 }

$detail = ($checkOutput | ForEach-Object { $_.ToString().Trim() } | Where-Object { $_ }) -join ' '
if ([string]::IsNullOrWhiteSpace($detail)) { $detail = 'the index is missing or stale' }
Write-HookContext "Graphify is configured, but its index is not ready ($detail). Refresh it with the graphify skill before querying the graph."
exit 0
