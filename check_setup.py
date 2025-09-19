#!/usr/bin/env python3
"""
Installation and setup verification script.
"""

import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def check_dependencies():
    """Check if required Python packages are installed."""
    required_packages = [
        'gitpython',
        'pydriller',
        'click',
        'flask',
        'flask_cors'
    ]

    missing_packages = []

    for package in required_packages:
        try:
            # Try importing with different possible names
            if package == 'flask_cors':
                __import__('flask_cors')
            elif package == 'gitpython':
                __import__('git')
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError as e:
            missing_packages.append(package)
            print(f"❌ {package} - {str(e)}")

    if missing_packages:
        print(f"\nMissing packages: {', '.join(missing_packages)}")
        print("Install with: pip install -r requirements.txt")
        print("Or if using virtual environment: .venv\\Scripts\\pip.exe install -r requirements.txt")
        print("\nNote: Make sure you're running this script with the same Python environment")
        print("where you installed the packages.")
        return False

    return True

def check_git():
    """Check if Git is installed."""
    try:
        result = subprocess.run(['git', '--version'],
                              capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        print(f"✅ {version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed or not in PATH")
        return False

def check_node():
    """Check if Node.js is installed."""
    try:
        result = subprocess.run(['node', '--version'],
                              capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        print(f"✅ Node.js {version}")

        # Check npm
        result = subprocess.run(['npm', '--version'],
                              capture_output=True, text=True, check=True)
        npm_version = result.stdout.strip()
        print(f"✅ npm {npm_version}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js/npm is not installed or not in PATH")
        print("   Download from: https://nodejs.org/")
        print("   Or install with: choco install nodejs")
        return False

def check_project_structure():
    """Check if project structure is correct."""
    required_files = [
        'requirements.txt',
        'setup.py',
        'README.md',
        'backend/src/__init__.py',
        'backend/src/analyzer.py',
        'backend/src/exporter.py',
        'backend/src/main.py',
        'frontend/package.json',
        'frontend/src/App.js',
        'frontend/src/index.js',
        'cli/src/main.py'
    ]

    missing_files = []

    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
            print(f"❌ {file_path}")
        else:
            print(f"✅ {file_path}")

    if missing_files:
        print(f"\nMissing files: {', '.join(missing_files)}")
        return False

    return True

def main():
    """Run all checks."""
    print("🔍 Checking Codebase Timeline Visualizer setup...\n")

    checks = [
        ("Python Version", check_python_version),
        ("Git Installation", check_git),
        ("Node.js Installation", check_node),
        ("Python Dependencies", check_dependencies),
        ("Project Structure", check_project_structure)
    ]

    results = []

    for name, check_func in checks:
        print(f"\n📋 {name}:")
        result = check_func()
        results.append(result)

    print("\n" + "="*50)

    if all(results):
        print("🎉 All checks passed! You're ready to use Codebase Timeline Visualizer.")
        print("\nNext steps:")
        print("1. Try the example: python example.py")
        print("2. Start the web interface: python -m cli.src.main serve")
        print("3. Analyze a repository: python -m cli.src.main analyze /path/to/repo")
        print("\nFor development:")
        print("- Run tests: python -m pytest backend/tests/")
        print("- Start frontend dev server: cd frontend && npm start")
    else:
        print("❌ Some checks failed. Please fix the issues above and try again.")
        print("\nCommon fixes:")
        print("- For Python packages: pip install -r requirements.txt")
        print("- For Node.js: Install from https://nodejs.org/")
        print("- For virtual environment: Use .venv\\Scripts\\python.exe check_setup.py")
        print("\nRe-run this script after fixing issues.")
        return 1

    return 0

if __name__ == '__main__':
    exit(main())