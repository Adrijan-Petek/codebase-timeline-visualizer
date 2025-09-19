# Setup Troubleshooting Guide

This guide helps you resolve common setup issues with the Codebase Timeline Visualizer.

## 🚀 Quick Setup (Windows)

### Option 1: Use the Setup Helper (Recommended)
```batch
# Double-click setup.bat or run in PowerShell:
.\setup.bat
```

### Option 2: Manual Setup
```batch
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
.venv\Scripts\activate

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Run setup check
python check_setup.py
```

## 🔧 Common Issues & Solutions

### Issue: "Node.js/npm is not installed or not in PATH"

**Symptoms:**
```
❌ Node.js/npm is not installed or not in PATH
   Download from: https://nodejs.org/
   Or install with: choco install nodejs
```

**Solutions:**

#### Option A: Install Node.js (Recommended)
1. Download from [nodejs.org](https://nodejs.org/)
2. Run the installer
3. Restart your terminal/command prompt
4. Run setup check again

#### Option B: Install with Chocolatey (Windows)
```batch
# Install Chocolatey (if not already installed)
# Visit: https://chocolatey.org/install

# Install Node.js
choco install nodejs

# Refresh environment
refreshenv

# Verify installation
node --version
npm --version
```

#### Option C: Add to PATH Manually
1. Find Node.js installation directory (usually `C:\Program Files\nodejs\`)
2. Add it to your system PATH:
   - Windows Search → "Environment Variables"
   - System Properties → "Environment Variables"
   - Edit "Path" variable
   - Add: `C:\Program Files\nodejs\`
3. Restart terminal and run setup check

### Issue: "Python packages not found"

**Symptoms:**
```
❌ gitpython - No module named 'git'
❌ pydriller - No module named 'pydriller'
```

**Solutions:**

#### Option A: Install in Virtual Environment (Recommended)
```batch
# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run setup check
python check_setup.py
```

#### Option B: Install Globally
```batch
# Install dependencies globally
pip install -r requirements.txt

# Run setup check
python check_setup.py
```

#### Option C: Use Correct Python Interpreter
```batch
# Make sure you're using the virtual environment Python
.venv\Scripts\python.exe check_setup.py
```

### Issue: "Git is not installed or not in PATH"

**Symptoms:**
```
❌ Git is not installed or not in PATH
```

**Solutions:**

#### Option A: Install Git
1. Download from [git-scm.com](https://git-scm.com/)
2. Run the installer with default options
3. Restart terminal
4. Verify: `git --version`

#### Option B: Install with Chocolatey
```batch
choco install git
refreshenv
git --version
```

### Issue: "Python 3.8 or higher is required"

**Symptoms:**
```
❌ Python 3.8 or higher is required
```

**Solutions:**

#### Option A: Install Python 3.8+
1. Download from [python.org](https://python.org/)
2. Make sure to check "Add Python to PATH" during installation
3. Restart terminal
4. Verify: `python --version`

#### Option B: Use Python Launcher (Windows)
```batch
# Use Python 3.8+ explicitly
py -3.8 --version
py -3.9 --version
py -3.10 --version
```

## 🧪 Testing Your Setup

### Run the Setup Check
```batch
# Using batch file
.\setup.bat

# Or manually
.venv\Scripts\python.exe check_setup.py
```

### Test Basic Functionality
```batch
# Activate virtual environment
.venv\Scripts\activate

# Test CLI
python -m cli.src.main --help

# Test analyzer (create a test repo first)
mkdir test-repo
cd test-repo
git init
echo "print('test')" > test.py
git add .
git commit -m "Test commit"
cd ..
python -m cli.src.main analyze ./test-repo
```

### Test Web Interface
```batch
# Start the server
python -m cli.src.main serve

# Open browser to http://localhost:3001
```

## 📁 Project Structure Verification

The setup check verifies these files exist:
- ✅ `requirements.txt`
- ✅ `setup.py`
- ✅ `README.md`
- ✅ `backend/src/__init__.py`
- ✅ `backend/src/analyzer.py`
- ✅ `backend/src/exporter.py`
- ✅ `backend/src/main.py`
- ✅ `frontend/package.json`
- ✅ `frontend/src/App.js`
- ✅ `frontend/src/index.js`
- ✅ `cli/src/main.py`

## 🔍 Advanced Troubleshooting

### Check Python Path
```batch
# See which Python is being used
where python
python --version

# Check virtual environment
.venv\Scripts\python.exe --version
```

### Check Package Installation
```batch
# List installed packages
.venv\Scripts\pip.exe list

# Check specific package
.venv\Scripts\python.exe -c "import git; print('gitpython OK')"
.venv\Scripts\python.exe -c "import pydriller; print('pydriller OK')"
```

### Check Node.js Path
```batch
# Check Node.js installation
where node
where npm
node --version
npm --version
```

### Environment Variables
```batch
# Check PATH
echo %PATH%

# Check Python environment
.venv\Scripts\python.exe -c "import sys; print(sys.path)"
```

## 📞 Getting Help

If you're still having issues:

1. **Check the logs** - Look for error messages in terminal output
2. **Verify versions** - Ensure all tools meet minimum requirements
3. **Restart terminal** - Sometimes PATH changes need a restart
4. **Check permissions** - Make sure you have write access to the directory

## 🎯 Minimum Requirements

- **Python**: 3.8 or higher
- **Git**: Any recent version
- **Node.js**: 16 or higher (for frontend development)
- **OS**: Windows 10+, macOS 10.15+, Ubuntu 18.04+

## 🚀 Next Steps

Once setup is complete:
1. Run `python example.py` to test with sample data
2. Analyze your own repository: `python -m cli.src.main analyze /path/to/repo`
3. Start the web interface: `python -m cli.src.main serve`
4. Visit http://localhost:3001 to see your timeline!

---

**Need more help?** Check the [main README](README.md) or create an issue on GitHub.