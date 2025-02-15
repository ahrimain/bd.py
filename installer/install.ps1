Write-Output "installing bd.py"
Invoke-WebRequest https://github.com/ahrimain/bd.py/raw/main/run.py -OutFile "./run.py"
Invoke-WebRequest https://github.com/ahrimain/bd.py/raw/main/run.ps1 -OutFile "./run.ps1"
Invoke-WebRequest https://github.com/ahrimain/bd.py/raw/main/setup.ps1 -OutFile "./setup.ps1"
mkdir src
Set-Location src
Invoke-WebRequest https://raw.githubusercontent.com/ahrimain/bd.py/main/src/builder.py -OutFile "./builder.py"