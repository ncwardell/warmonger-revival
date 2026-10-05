param(
    [string]$BindAddress = '127.0.0.1',
    [switch]$QuestTest
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
$previousQuestMode = $env:WARMONGER_QUEST_TEST
try {
    $env:WARMONGER_QUEST_TEST = if ($QuestTest) { '1' } else { '0' }
    if ($QuestTest) {
        Write-Host 'Quest experiment: quests 1-7, the Training Camp portal, and two Chepa officers.'
    }
    & python -u -B (Join-Path $repoRoot 'server\stub.py') $BindAddress
    if ($LASTEXITCODE -ne 0) { throw "Server exited with code $LASTEXITCODE" }
}
finally {
    $env:WARMONGER_QUEST_TEST = $previousQuestMode
}
