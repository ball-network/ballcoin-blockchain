param (
    [Parameter(Mandatory=$true)][string]$version
)
$env:BALL_INSTALLER_VERSION = $version

Set-Location -Path ".\ballcoin-blockchain-gui" -PassThru

Write-Output "   ---"
Write-Output "Prepare Electron packager"
Write-Output "   ---"
npm install --save-dev electron-winstaller
npm install -g electron-packager
npm install
npm audit fix

Write-Output "   ---"
Write-Output "Electron package Windows Installer"
Write-Output "   ---"
npm run build
If ($LastExitCode -gt 0){
    Throw "npm run build failed!"
}

Write-Output "   ---"
Write-Output "Increase the stack for ball command for (ball plots create) chiapos limitations"
# editbin.exe needs to be in the path
editbin.exe /STACK:8000000 daemon\ball.exe
Write-Output "   ---"

$appName = "SIT"
$packageVersion = $version
$packageName = "$appName-$packageVersion"

Write-Output "packageName is $packageName"

Write-Output "   ---"
Write-Output "electron-packager"
electron-packager . $appName --asar.unpack="**\daemon\**" --overwrite --icon=.\src\assets\img\ball.ico --app-version=$packageVersion
Write-Output "   ---"

Write-Output "   ---"
Write-Output "node winstaller.js"
node winstaller.js



#Write-Output "   ---"
#Write-Output "Add timestamp and verify signature"
#Write-Output "   ---"
#signtool.exe timestamp /v /t http://timestamp.comodoca.com/ .\release-builds\windows-installer\$appNameSetup-$packageVersion.exe
#signtool.exe verify /v /pa .\release-builds\windows-installer\$appNameSetup-$packageVersion.exe
 

git status

Write-Output "   ---"
Write-Output "Windows Installer complete"
Write-Output "   ---"
Set-Location -Path "..\" -PassThru