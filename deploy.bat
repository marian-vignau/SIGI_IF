echo copy to server

set destiny="\\Nas01\NAS01_Disco01\SIGI-IF"

robocopy "installer\dist\SIGI_IF.exe" %destiny% /E /XF *.db /XD backup data

if not exist "%destiny%\data" mkdir "%destiny%\data"