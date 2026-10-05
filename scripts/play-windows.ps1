param(
    [string]$GameDir = (Join-Path (Split-Path $PSScriptRoot -Parent) 'client'),
    [ValidatePattern('^[A-Za-z0-9_-]{1,31}$')]
    [string]$Account = 'player',
    [string]$ServerAddress = '127.0.0.1'
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path $PSScriptRoot -Parent
$gamePath = (Resolve-Path -LiteralPath $GameDir).Path
$clientExe = Join-Path $gamePath 'Client.exe'
$serverConfig = Join-Path $gamePath 'Data\config\serverlist.sof'
if (-not (Test-Path -LiteralPath $clientExe)) {
    throw "Client.exe was not found in $gamePath. Copy your Steam game folder to $repoRoot\client first, or pass -GameDir."
}
if (-not (Test-Path -LiteralPath "$serverConfig.revival-backup")) {
    Copy-Item -LiteralPath $serverConfig -Destination "$serverConfig.revival-backup"
}
& python (Join-Path $repoRoot 'tools\sof.py') point $serverConfig $ServerAddress
if ($LASTEXITCODE -ne 0) { throw 'Could not update the server address.' }

# Client option parser FUN_00407510 takes the token from character 8 of the
# same argument. A separate '-ologin alice' leaves token mode disabled.
$clientArguments = @('-nosg', '-windowed', '-width', '1600', '-height', '900', "-ologin=$Account")
# This is the interactive game window; the dead patcher is deliberately skipped.
Start-Process -FilePath $clientExe -WorkingDirectory $gamePath -ArgumentList $clientArguments
