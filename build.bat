@echo off

set root_path=%~dp0
set log=%1

python3 "%root_path%build.py" %log%

echo "[RUN INFO]: "
.\out\hello.exe

pause
