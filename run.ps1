Write-Output "cheking .output"
if (Test-Path -Path "./.output") {
    Write-Output ".output already exists"
    Write-Output "removing"
    Remove-Item .output -Recurse
}
Write-Output "making .output"
mkdir .output
Write-Output "made .output"


Write-Output "cheking pages"
if (Test-Path -Path "./pages") {
    Write-Output "pages exists"
} else {
    Write-Output "no pages \n making pages"
    mkdir pages
    Write-Output "made pages"
}

Write-Output "building"
mkdir .build
New-Item .build/assets
New-Item .build/pages
python3 run.py
Remove-Item .build -Recurse