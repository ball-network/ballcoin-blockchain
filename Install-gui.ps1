$ErrorActionPreference = "Stop"

if ($null -eq (Get-ChildItem env:VIRTUAL_ENV -ErrorAction SilentlyContinue))
{
    Write-Output "This script requires that the Chia Python virtual environment is activated."
    Write-Output "Execute '.\venv\Scripts\Activate.ps1' before running."
    Exit 1
}

if ($null -eq (Get-Command node -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find Node.js"
    Exit 1
}
Push-Location
try {
    Set-Location ballcoin-blockchain-gui

    $ErrorActionPreference = "SilentlyContinue"
    npm install --loglevel=error
    npm audit fix
    npm run build

    Write-Output ""
    Write-Output "Chia blockchain Install-gui.ps1 completed."
    Write-Output ""
    Write-Output "Type 'cd ballcoin-blockchain-gui' and then 'npm run electron' to start the GUI."
} finally {
    Pop-Location
}
