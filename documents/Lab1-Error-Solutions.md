# Lab1 - General Setup Error Solutions

This document captures common errors and troubleshooting solutions for general lab setup, Python environment configuration, and Azure connectivity issues.

## Table of Contents
1. [Python Environment Issues](#python-environment-issues)
2. [Virtual Environment Problems](#virtual-environment-problems)
3. [Package Installation Errors](#package-installation-errors)
4. [Azure Authentication Issues](#azure-authentication-issues)
5. [File Path and Directory Issues](#file-path-and-directory-issues)
6. [Import and Module Errors](#import-and-module-errors)
7. [General Setup Troubleshooting](#general-setup-troubleshooting)

---

## Python Environment Issues

### Error: Python Command Not Found
```
'python' is not recognized as an internal or external command
```

### Solutions
1. **Check Python Installation**
   ```powershell
   python --version
   # or
   python3 --version
   # or
   py --version
   ```

2. **Add Python to PATH** (Windows)
   - Open "Environment Variables" from System Properties
   - Add Python installation directory to PATH
   - Common locations: `C:\Python311\`, `C:\Users\username\AppData\Local\Programs\Python\Python311\`

3. **Use Python Launcher** (Windows)
   ```powershell
   py -m pip install package_name
   py script.py
   ```

### Multiple Python Versions Conflict
```
ModuleNotFoundError: No module named 'package_name'
```

### Solutions
1. **Check Active Python Version**
   ```powershell
   python --version
   where python
   ```

2. **Use Specific Python Version**
   ```powershell
   py -3.11 -m pip install package_name
   py -3.11 script.py
   ```

---

## Virtual Environment Problems

### Error: Virtual Environment Not Activating
```
.\venv\Scripts\activate : cannot be loaded because running scripts is disabled
```

### Solutions
1. **Enable Script Execution** (PowerShell)
   ```powershell
   # Check current policy
   Get-ExecutionPolicy
   
   # Set policy for current user
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   # Or temporarily bypass
   PowerShell -ExecutionPolicy Bypass
   ```

2. **Alternative Activation Methods**
   ```powershell
   # Method 1: Direct path
   C:\path\to\venv\Scripts\Activate.ps1
   
   # Method 2: Command prompt style
   venv\Scripts\activate.bat
   
   # Method 3: Using Python
   python -m venv venv --prompt lab_env
   ```

### Virtual Environment Creation Fails
```
Error: Unable to create virtual environment
```

### Solutions
1. **Create with Full Path**
   ```powershell
   python -m venv C:\MyREPO\Workshop\gen-ai-labs\Lab1\venv
   ```

2. **Use Different Python Version**
   ```powershell
   py -3.11 -m venv venv
   ```

3. **Clear and Recreate**
   ```powershell
   Remove-Item -Recurse -Force venv
   python -m venv venv
   ```

---

## Package Installation Errors

### Error: pip not found or outdated
```
'pip' is not recognized as an internal or external command
pip: command not found
```

### Solutions
1. **Use Python Module Method**
   ```powershell
   python -m pip install package_name
   python -m pip install --upgrade pip
   ```

2. **Reinstall pip**
   ```powershell
   python -m ensurepip --upgrade
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python get-pip.py
   ```

### Permission Errors During Installation
```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

### Solutions
1. **Use User Installation**
   ```powershell
   pip install --user package_name
   ```

2. **Run as Administrator**
   - Right-click PowerShell → "Run as Administrator"
   - Or use elevated command prompt

3. **Virtual Environment** (Recommended)
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install package_name
   ```

### SSL Certificate Errors
```
SSL: CERTIFICATE_VERIFY_FAILED
```

### Solutions
1. **Upgrade pip and certificates**
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install --upgrade certifi
   ```

2. **Temporary workaround** (Not recommended for production)
   ```powershell
   pip install --trusted-host pypi.org --trusted-host pypi.python.org package_name
   ```

---

## Azure Authentication Issues

### Error: Azure CLI Not Installed
```
'az' is not recognized as an internal or external command
```

### Solutions
1. **Install Azure CLI**
   - Download from: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
   - Or use PowerShell:
   ```powershell
   Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi
   Start-Process msiexec.exe -ArgumentList '/I AzureCLI.msi /quiet' -Wait
   ```

### Azure Login Issues
```
ERROR: Please run 'az login' to setup account.
```

### Solutions
1. **Interactive Login**
   ```powershell
   az login
   ```

2. **Device Code Login** (for restricted environments)
   ```powershell
   az login --use-device-code
   ```

3. **Service Principal Login**
   ```powershell
   az login --service-principal -u <app-id> -p <password> --tenant <tenant>
   ```

### Subscription Access Issues
```
ERROR: The subscription 'xxx' doesn't exist or you don't have access.
```

### Solutions
1. **List Available Subscriptions**
   ```powershell
   az account list --output table
   ```

2. **Set Specific Subscription**
   ```powershell
   az account set --subscription "subscription-name-or-id"
   ```

---

## File Path and Directory Issues

### Error: File Not Found
```
FileNotFoundError: [Errno 2] No such file or directory: 'filename.py'
```

### Solutions
1. **Check Current Directory**
   ```powershell
   pwd  # Current directory
   ls   # List files
   ```

2. **Navigate to Correct Directory**
   ```powershell
   cd C:\MyREPO\Workshop\gen-ai-labs\Lab1
   ```

3. **Use Absolute Paths**
   ```python
   import os
   script_dir = os.path.dirname(os.path.abspath(__file__))
   file_path = os.path.join(script_dir, 'filename.py')
   ```

### Path Separator Issues (Windows vs Unix)
```
FileNotFoundError: Invalid path separators
```

### Solutions
1. **Use os.path.join()**
   ```python
   import os
   path = os.path.join('folder', 'subfolder', 'file.txt')
   ```

2. **Use pathlib** (Modern approach)
   ```python
   from pathlib import Path
   path = Path('folder') / 'subfolder' / 'file.txt'
   ```

---

## Import and Module Errors

### Error: Module Not Found
```
ModuleNotFoundError: No module named 'module_name'
```

### Troubleshooting Steps
1. **Check Virtual Environment**
   ```powershell
   # Ensure virtual environment is activated
   .\venv\Scripts\activate
   
   # Check installed packages
   pip list
   ```

2. **Install Missing Package**
   ```powershell
   pip install module_name
   # or from requirements.txt
   pip install -r requirements.txt
   ```

3. **Check Python Path**
   ```python
   import sys
   print(sys.path)
   ```

### Common Missing Packages and Solutions

| Error | Package | Installation |
|-------|---------|-------------|
| `No module named 'dotenv'` | python-dotenv | `pip install python-dotenv` |
| `No module named 'openai'` | openai | `pip install openai` |
| `No module named 'azure'` | azure-* | `pip install azure-identity azure-storage-blob` |
| `No module named 'requests'` | requests | `pip install requests` |
| `No module named 'pandas'` | pandas | `pip install pandas` |
| `No module named 'numpy'` | numpy | `pip install numpy` |

---

## General Setup Troubleshooting

### Complete Environment Setup Checklist

1. **Python Installation**
   - [ ] Python 3.8+ installed
   - [ ] Python added to PATH
   - [ ] pip working (`python -m pip --version`)

2. **Project Setup**
   - [ ] Correct directory (`cd Lab1` or `cd Lab2`)
   - [ ] Virtual environment created (`python -m venv venv`)
   - [ ] Virtual environment activated (`.\venv\Scripts\activate`)
   - [ ] Dependencies installed (`pip install -r requirements.txt`)

3. **Configuration Files**
   - [ ] `.env` file exists and configured
   - [ ] No conflicting environment variables
   - [ ] Correct file permissions

4. **Azure Resources**
   - [ ] Azure subscription active
   - [ ] Required Azure resources deployed
   - [ ] Proper authentication configured
   - [ ] Network connectivity to Azure

### Quick Diagnostic Commands

```powershell
# Environment check
python --version
pip --version
az --version

# Project structure check
ls
cat .env  # Check configuration
cat requirements.txt  # Check dependencies

# Python environment check
python -c "import sys; print(sys.executable)"
python -c "import sys; print(sys.path)"
pip list  # Show installed packages
```

### Clean Setup Script

Create a `setup.ps1` script for easy environment setup:

```powershell
# setup.ps1
Write-Host "Setting up Lab environment..." -ForegroundColor Green

# Check Python
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Create virtual environment
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\activate

# Install dependencies
if (Test-Path "requirements.txt") {
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    pip install -r requirements.txt
} else {
    Write-Host "No requirements.txt found, installing basic packages..." -ForegroundColor Yellow
    pip install python-dotenv openai requests
}

# Check configuration
if (Test-Path ".env") {
    Write-Host "Configuration file found: .env" -ForegroundColor Green
} else {
    Write-Host "WARNING: No .env file found. Copy example.env to .env and configure." -ForegroundColor Yellow
}

Write-Host "Setup complete! Virtual environment is activated." -ForegroundColor Green
```

Usage:
```powershell
.\setup.ps1
```

---

## Emergency Reset Procedures

### Complete Environment Reset
```powershell
# Stop all Python processes
taskkill /f /im python.exe

# Remove virtual environment
Remove-Item -Recurse -Force venv

# Clear pip cache
python -m pip cache purge

# Recreate environment
python -m venv venv
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Clear All Environment Variables
```powershell
# Clear Azure-related environment variables
Get-ChildItem Env: | Where-Object Name -like "*AZURE*" | ForEach-Object { Remove-Item "Env:$($_.Name)" }

# Or selectively clear
$env:AZURE_OPENAI_ENDPOINT = $null
$env:AZURE_OPENAI_API_KEY = $null
```

---

## Support Resources

- **Python Documentation**: https://docs.python.org/3/
- **pip Documentation**: https://pip.pypa.io/en/stable/
- **Virtual Environments Guide**: https://docs.python.org/3/tutorial/venv.html
- **Azure CLI Documentation**: https://docs.microsoft.com/en-us/cli/azure/
- **PowerShell Execution Policy**: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy