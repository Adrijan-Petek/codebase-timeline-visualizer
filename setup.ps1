# Codebase Timeline Visualizer Setup Helper
# This script helps run the setup check with the correct Python environment

Write-Host "🚀 Codebase Timeline Visualizer Setup Helper" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
$venvPath = ".venv\Scripts\python.exe"
if (-not (Test-Path $venvPath)) {
    Write-Host "❌ Virtual environment not found at .venv" -ForegroundColor Red
    Write-Host "Please run: python -m venv .venv"
    Write-Host "Then: .venv\Scripts\pip.exe install -r requirements.txt"
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✅ Virtual environment found" -ForegroundColor Green
Write-Host ""

# Run setup check with virtual environment
Write-Host "🔍 Running setup verification..." -ForegroundColor Yellow
& $venvPath check_setup.py

# Check exit code
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 Setup complete! You can now use the application." -ForegroundColor Green
    Write-Host ""
    Write-Host "Quick start commands:" -ForegroundColor Cyan
    Write-Host "  - Analyze a repo: .venv\Scripts\python.exe -m cli.src.main analyze C:\path\to\repo" -ForegroundColor White
    Write-Host "  - Start web UI: .venv\Scripts\python.exe -m cli.src.main serve" -ForegroundColor White
    Write-Host "  - Run example: .venv\Scripts\python.exe example.py" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "❌ Setup check failed. Please fix the issues above." -ForegroundColor Red
    Write-Host "Common solutions:" -ForegroundColor Yellow
    Write-Host "  - Install Node.js from https://nodejs.org/" -ForegroundColor White
    Write-Host "  - Run: .venv\Scripts\pip.exe install -r requirements.txt" -ForegroundColor White
    Write-Host "  - Make sure Git is installed and in PATH" -ForegroundColor White
}

Write-Host ""
Read-Host "Press Enter to exit"