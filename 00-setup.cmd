@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "scripts\setup.ps1"
set "result=%errorlevel%"
if not "%result%"=="0" pause
exit /b %result%
