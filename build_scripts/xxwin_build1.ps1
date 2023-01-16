# $env:path should contain a path to editbin.exe and signtool.exe

#$ErrorActionPreference = "Stop"

Write-Output "   ---"
Write-Output "clean source"
Write-Output "   ---"
git clean -fdx
Set-Location -Path ".\ballcoin-blockchain-gui" -PassThru
git clean -fdx
Set-Location -Path "../" -PassThru


mkdir build_scripts\win_build
Set-Location -Path ".\build_scripts\win_build" -PassThru

git status

Write-Output "   ---"
Write-Output "curl miniupnpc"
Write-Output "   ---"
Invoke-WebRequest -Uri "https://pypi.chia.net/simple/miniupnpc/miniupnpc-2.1-cp37-cp37m-win_amd64.whl" -OutFile "miniupnpc-2.1-cp37-cp37m-win_amd64.whl"
Write-Output "Using win_amd64 python 3.7 wheel from https://github.com/miniupnp/miniupnp/pull/475 (2.2.0-RC1)"
If ($LastExitCode -gt 0){
    Throw "Failed to download miniupnpc!"
}
else
{
    Set-Location -Path "../../" -PassThru
    Write-Output "miniupnpc download successful."
}

Write-Output "   ---"
Write-Output "Create venv - python3.7 or 3.8 is required in PATH"
Write-Output "   ---"
python -m venv venv
. .\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install wheel pep517
pip install pywin32
pip install pyinstaller==4.2
pip install setuptools_scm

pip install bitstring --no-binary :all:
pip install keyring==23.0.1 --no-binary :all:
pip install keyrings.cryptfile==1.3.4 --no-binary :all:


Write-Output "   ---"
Write-Output "Build ballcoin-blockchain wheels"
Write-Output "   ---"
pip wheel --use-pep517 --extra-index-url https://pypi.chia.net/simple/ -f . --wheel-dir=.\build_scripts\win_build .

Write-Output "   ---"
Write-Output "Install ballcoin-blockchain wheels into venv with pip"
Write-Output "   ---"

Write-Output "pip install miniupnpc"
Set-Location -Path ".\build_scripts" -PassThru
pip install --no-index --find-links=.\win_build\ miniupnpc
# Write-Output "pip install setproctitle"
# pip install setproctitle==1.2.2

Write-Output "pip install ballcoin-blockchain"
pip install --no-index --find-links=.\win_build\ ballcoin-blockchain

Write-Output "   ---"
Write-Output "Use pyinstaller to create ball .exe's"
Write-Output "   ---"
$SPEC_FILE = (python -c 'import ball; print(ball.PYINSTALLER_SPEC_PATH)') -join "`n"
pyinstaller --log-level INFO $SPEC_FILE

Write-Output "   ---"
Write-Output "Copy ball executables to ballcoin-blockchain-gui\"
Write-Output "   ---"
Copy-Item "dist\daemon" -Destination "..\ballcoin-blockchain-gui\" -Recurse

cd ../
deactivate
