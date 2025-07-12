@echo off
cd /d %~dp0
setlocal

where python >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=python"
) else (
    where python3 >nul 2>nul
    if %errorlevel%==0 (
        set "PYTHON_CMD=python3"
    ) else (
        echo [HATA] python veya python3 bulunamadi.
        pause
        exit /b
    )
)

:MENU
cls
echo ===========================
echo    Rappelz Bot Yonetici
echo ===========================
echo [1] Ayarlari Ac (GUI)
echo [2] Botu Baslat (farm.py)
echo [Q] Cikis
echo.
set /p choice="Seciminiz: "

if /I "%choice%"=="1" (
    %PYTHON_CMD% config_gui.py
    echo.
    echo [!] GUI kapatildi veya hata alindi. Devam etmek icin bir tusa basin...
    pause >nul
    goto MENU
) else if /I "%choice%"=="2" (
    %PYTHON_CMD% farm.py
    echo.
    echo [!] Bot sonlandirildi veya hata alindi. Devam etmek icin bir tusa basin...
    pause >nul
    goto MENU
) else if /I "%choice%"=="Q" (
    exit /b
) else (
    echo Gecersiz secim.
    timeout /t 2 >nul
    goto MENU
)
