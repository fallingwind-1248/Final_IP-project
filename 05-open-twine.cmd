@echo off
setlocal
cd /d "%~dp0"
start "" "%LOCALAPPDATA%\Programs\Twine\Twine.exe" "--user-data-dir=%~dp0.local\twine-editor"
