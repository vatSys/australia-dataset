@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

echo Maestro Plugin DLL Unblock Utility
echo ===================================
echo.
echo This script will unblock all DLL files in the current directory and subdirectories.
echo Current directory: %CD%
echo.

:: Count DLL files in current directory and subdirectories
set "dllCount=0"
for /r %%F in ("*.dll") do (
    set /a dllCount+=1
)

if %dllCount% equ 0 (
    echo No DLL files found in the current directory or subdirectories.
    echo.
    echo Make sure you have placed this script in the same folder as the Maestro plugin DLLs.
    echo Expected location: Documents\vatSys Files\Profiles\[ProfileName]\Plugins\MaestroPlugin\
    goto :end
)

echo Found %dllCount% DLL file(s) to unblock:
for /r %%F in ("*.dll") do (
    echo   - %%F
)
echo.

:: Ask for user confirmation
set /p "confirm=Do you want to unblock these DLL files? (Y/N): "
if /i not "%confirm%"=="Y" if /i not "%confirm%"=="YES" (
    echo Operation cancelled by user.
    goto :end
)

echo.
echo Starting unblock process...
echo.

:: Unblock each DLL file in the current directory and subdirectories
for /r %%F in ("*.dll") do (
    echo Unblocking: %%F

    :: Use PowerShell to unblock the file
    powershell -Command "try { Unblock-File -Path '%%F' -ErrorAction Stop; Write-Host '  Unblocked successfully' } catch { Write-Host '  Failed to unblock: ' $_.Exception.Message }"
)

echo.
echo Unblocking complete!

:end
echo.
echo Press any key to exit...
pause >nul

ENDLOCAL