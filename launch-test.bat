@echo off
cd /d %~dp0
setlocal

:: Python yorumlayıcıyı bul
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

:: Yolu test et
echo [DEBUG] Secilen yorumlayici: %PYTHON_CMD%
echo [DEBUG] Aktif klasor: %CD%
echo [DEBUG] Calistirilacak dosya: %~dp0config_gui.py

:: Dosya var mi?
if not exist "%~dp0config_gui.py" (
    echo [HATA] config_gui.py bu klasorde bulunamadi!
    pause
    exit /b
)

:: Dosyayi calistir
%PYTHON_CMD% "%~dp0config_gui.py"

:: Pause ki terminal kapanmasin
echo.
echo [BILGI] Script tamamlandi. Terminali kapatmak icin bir tusa basin.
pause >nul
