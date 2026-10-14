$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
Set-Location -LiteralPath $root
& python -X utf8 (Join-Path $PSScriptRoot 'setup_tools.py')
if ($LASTEXITCODE -ne 0) { throw 'Tool setup failed.' }
$oldHttp = $env:HTTP_PROXY
$oldHttps = $env:HTTPS_PROXY
try {
    $proxy = Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' -ErrorAction SilentlyContinue
    if ($proxy.ProxyEnable -eq 1 -and $proxy.ProxyServer -match '^([^=;]+):(\d+)$') {
        $env:HTTP_PROXY = 'http://' + $proxy.ProxyServer
        $env:HTTPS_PROXY = $env:HTTP_PROXY
    }
    if (Test-Path -LiteralPath 'package-lock.json') { & npm.cmd ci --ignore-scripts } else { & npm.cmd install --ignore-scripts }
    if ($LASTEXITCODE -ne 0) { throw 'Development dependency setup failed.' }
} finally {
    $env:HTTP_PROXY = $oldHttp
    $env:HTTPS_PROXY = $oldHttps
}
& python -X utf8 (Join-Path $PSScriptRoot 'configure_twine.py')
if ($LASTEXITCODE -ne 0) { throw 'Twine project configuration failed.' }
$blenderConfig = Join-Path $root '.local\blender-config'
if (-not (Test-Path -LiteralPath (Join-Path $blenderConfig 'userpref.blend'))) {
    New-Item -ItemType Directory -Force -Path $blenderConfig | Out-Null
    $previousConfig = $env:BLENDER_USER_CONFIG
    try {
        $env:BLENDER_USER_CONFIG = $blenderConfig
        & (Join-Path $root '.tools\blender\blender-4.5.14-windows-x64\blender.exe') --background --factory-startup --python (Join-Path $PSScriptRoot 'configure_blender.py')
        if ($LASTEXITCODE -ne 0) { throw 'Blender project configuration failed.' }
    } finally { $env:BLENDER_USER_CONFIG = $previousConfig }
}
& (Join-Path $PSScriptRoot 'check_environment.ps1')
