@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"
node scripts/project.mjs compare
set "result=%errorlevel%"
if not "%result%"=="0" pause
exit /b %result%
