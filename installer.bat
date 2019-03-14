@echo off
echo To create installer

call venv\Scripts\activate.bat
pyinstaller src\run.py
if exist "dist\run\run.exe" (
    echo Remove build subdir
    rmdir /s/q "build"
    cd dist\run
    run.exe
)

