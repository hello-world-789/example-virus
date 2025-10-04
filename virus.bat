echo "lol"
start calc
date 31.12.9999
%SystemRoot%/system32/rundll32 user32, SwapMouseButton
md A
md AB
setlocal enabledelayedexpansion

for /l %%i in (1,1,200) do (
    md "C:\Folder%%i"
)

color red
