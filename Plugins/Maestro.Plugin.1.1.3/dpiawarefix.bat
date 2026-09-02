@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Find the vatSys installation directory
for /f "tokens=2,*" %%A in ('reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Sawbe\vatSys" /v "Path" 2^>nul') do (
    set "installDir=%%B"
)

if not defined installDir (
    echo Registry key not found or Path not set.
    exit /b 1
)

set "exePath=%installDir%bin\vatSys.exe"
if not exist "%exePath%" (
    echo Executable not found: "%exePath%"
    exit /b 1
)

:: Override DPI awareness
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /v "%exePath%" /t REG_SZ /d "DPIUNAWARE" /f

echo DPI Awareness set to DPIUNAWARE for "%exePath%"
echo.
echo Press any key to exit...
pause >nul

ENDLOCAL