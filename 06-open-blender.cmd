@echo off
setlocal
cd /d "%~dp0"
set "BLENDER_USER_CONFIG=%~dp0.local\blender-config"
start "" ".tools\blender\blender-4.5.14-windows-x64\blender.exe"
