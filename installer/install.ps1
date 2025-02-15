Write-Output "installing bd.py"
Invoke-WebRequest -q https://github.com/ahrimain/bd.py/raw/main/run.py
Invoke-WebRequest -q https://github.com/ahrimain/bd.py/raw/main/run.ps1
Invoke-WebRequest -q https://github.com/ahrimain/bd.py/raw/main/setup.ps1
mkdir src
Set-Location src
Invoke-WebRequest -q https://raw.githubusercontent.com/ahrimain/bd.py/main/src/builder.py