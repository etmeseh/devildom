@echo off
cd /d %~dp0
where python >nul 2>nul
if %errorlevel%==0 (
    python config_gui.py
) else (
    python3 config_gui.py
)
pause
