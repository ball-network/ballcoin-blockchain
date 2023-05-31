# $env:path should contain a path to editbin.exe and signtool.exe

$ErrorActionPreference = "Stop"


if (-not (Test-Path env:BALL_INSTALLER_VERSION)) {
  $env:BALL_INSTALLER_VERSION = '0.0.0'
  Write-Output "WARNING: No environment variable BALL_INSTALLER_VERSION set. Using 0.0.0"
}

Write-Output "   ---"
Write-Output "Use pyinstaller to create ball .exe's"
Write-Output "   ---"
$SPEC_FILE = (python -c 'import ball; print(ball.PYINSTALLER_SPEC_PATH)') -join "`n"
pyinstaller --log-level INFO $SPEC_FILE
Write-Output "   ---"

Write-Output "Copy ball executables to ballcoin-blockchain-gui\"
Write-Output "   ---"
Copy-Item "dist\daemon" -Destination "..\ballcoin-blockchain-gui\packages\gui\" -Recurse


Write-Output "   ---"
Write-Output "Setup npm packager"
Write-Output "   ---"
Set-Location -Path ".\npm_windows" -PassThru
npm ci
$Env:Path = $(npm bin) + ";" + $Env:Path

Set-Location -Path "..\..\" -PassThru
If ($env:HAS_SECRET) {
    $env:CSC_LINK = Join-Path "." "win_code_sign_cert.p12" -Resolve
}

Write-Output "   ---"
Write-Output "Prepare Electron packager"
Write-Output "   ---"
$Env:NODE_OPTIONS = "--max-old-space-size=3000"

# Change to the GUI directory
Set-Location -Path "ballcoin-blockchain-gui\packages\gui" -PassThru


$packageVersion = "$env:BALL_INSTALLER_VERSION"
$packageName = "Ball-$packageVersion"

Write-Output "packageName is $packageName"


Write-Output "   ---"
Write-Output "electron-builder"
electron-builder build --win --x64 --config.productName="Ball"
Get-ChildItem dist\win-unpacked\resources
Write-Output "   ---"

If ($env:HAS_SECRET) {
   Write-Output "   ---"
   Write-Output "Verify signature"
   Write-Output "   ---"
   signtool.exe verify /v /pa .\dist\BallSetup-$packageVersion.exe
   }   Else    {
   Write-Output "Skipping verify signatures - no authorization to install certificates"
}
if (-not (Test-Path env:GITHUB_WORKSPACE)) {
  $env:GITHUB_WORKSPACE = "..\..\.."
}
Write-Output "   ---"
Write-Output "Moving final installers to expected location"
Write-Output "   ---"
Copy-Item ".\dist\win-unpacked" -Destination "$env:GITHUB_WORKSPACE\ballcoin-blockchain-gui\Ball-win32-x64" -Recurse
mkdir "$env:GITHUB_WORKSPACE\ballcoin-blockchain-gui\release-builds\windows-installer" -ea 0
Copy-Item ".\dist\BallSetup-$packageVersion.exe" -Destination "$env:GITHUB_WORKSPACE\ballcoin-blockchain-gui\release-builds\windows-installer"

Write-Output "   ---"
Write-Output "Windows Installer complete"
Write-Output "   ---"
