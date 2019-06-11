@echo off
rem  in
rem  venvSIGI\Lib\site-packages\PyInstaller\depend\bindepend.py
rem  line 905: where says: return none
rem  use: return r"C:\Program Files (x86)\Python37-32\python37.dll"
rem  last version of PyInstaller seems to fix this
rem  https://github.com/pyinstaller/pyinstaller/commit/80941bcdbfdb2baabdaafa023f1e2abbc45b0218
echo To create installer
if exist "installer" (
    rmdir /s/q "installer"
)

md installer
cd src
pyinstaller --distpath=..\installer\dist --workpath=..\installer\build run.spec
cd ..
if exist "installer\dist\run\run.exe" (
    echo Remove build subdir
    rmdir /s/q "installer\build"
)

