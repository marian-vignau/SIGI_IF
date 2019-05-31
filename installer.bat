@echo off
echo Creating installer
if exist "installer" (
    rmdir /s/q "installer"
)

call venv\Scripts\activate.bat
md installer
cd src


pyinstaller --icon=..\img\icon.ico --distpath ..\installer\dist --workpath ..\installer\build --windowed --name SIGI_IF.exe run.py
cd ..
if exist "installer\dist\run\SIGI_IF.exe" (
    echo Removingcd S build subdir
    rmdir /s/q "installer\build"
    call venv\Scripts\deactivate.bat
)

