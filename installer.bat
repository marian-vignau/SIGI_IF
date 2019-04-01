@echo off
echo To create installer
if exist "installer" (
    rmdir /s/q "installer"
)

call venv\Scripts\activate.bat
md installer
cd src
pyinstaller  --distpath ..\installer\dist --workpath ..\installer\build -w run.py
cd ..
if exist "installer\dist\run\run.exe" (
    echo Remove build subdir
    rmdir /s/q "installer\build"
    call venv\Scripts\deactivate.bat
)

