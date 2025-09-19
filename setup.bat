@echo off
REM Codebase Timeline Visualizer Setup Helper
REM This script helps run the setup check with the correct Python environment

echo 🚀 Codebase Timeline Visualizer Setup Helper
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\python.exe" (
    echo ❌ Virtual environment not found at .venv
    echo Please run: python -m venv .venv
    echo Then: .venv\Scripts\pip.exe install -r requirements.txt
    pause
    exit /b 1
)

echo ✅ Virtual environment found
echo.

REM Run setup check with virtual environment
echo 🔍 Running setup verification...
.venv\Scripts\python.exe check_setup.py

REM Check exit code
if %ERRORLEVEL% EQU 0 (
    echo.
    echo 🎉 Setup complete! You can now use the application.
    echo.
    echo Quick start commands:
    echo - Analyze a repo: .venv\Scripts\python.exe -m cli.src.main analyze C:\path\to\repo
    echo - Start web UI: .venv\Scripts\python.exe -m cli.src.main serve
    echo - Run example: .venv\Scripts\python.exe example.py
) else (
    echo.
    echo ❌ Setup check failed. Please fix the issues above.
    echo Common solutions:
    echo - Install Node.js from https://nodejs.org/
    echo - Run: .venv\Scripts\pip.exe install -r requirements.txt
    echo - Make sure Git is installed and in PATH
)

echo.
pause