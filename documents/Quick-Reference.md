# Quick Reference - Common Errors & Solutions

## 🚨 Emergency Fixes

### Python Not Working
```powershell
# Try these in order:
python --version
py --version
py -3.11 --version

# If none work, reinstall Python from python.org
```

### Virtual Environment Won't Activate
```powershell
# Enable PowerShell scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
.\venv\Scripts\activate
```

### Package Import Errors
```powershell
# Make sure you're in virtual environment
.\venv\Scripts\activate

# Install missing packages
pip install -r requirements.txt

# Or install specific package
pip install openai python-dotenv
```

### Azure OpenAI Connection Error
```powershell
# Check environment variables
python debug_env.py

# Clear conflicting variables
$env:AZURE_OPENAI_ENDPOINT = $null
$env:AZURE_OPENAI_API_KEY = $null

# Test connection
python diagnostic_tool.py
```

## 🔍 Quick Diagnostic Commands

```powershell
# Environment check
python --version && pip --version

# Project check
ls  # Should see .env, requirements.txt, venv/

# Virtual environment check
.\venv\Scripts\activate
pip list

# Azure check (in Python)
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(f'Endpoint: {os.getenv(\"AZURE_OPENAI_ENDPOINT\")}')"
```

## 🛠️ One-Command Fixes

### Reset Everything
```powershell
# Nuclear option - start fresh
Remove-Item -Recurse -Force venv
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Clear Azure Environment Variables
```powershell
# Clear all Azure variables
Get-ChildItem Env: | Where-Object Name -like "*AZURE*" | ForEach-Object { Remove-Item "Env:$($_.Name)" }
```

### Quick Environment Setup
```powershell
# All-in-one setup
python -m venv venv; .\venv\Scripts\activate; pip install openai python-dotenv requests
```

## 📱 Error Code Lookup

| Error Pattern | Cause | Fix |
|--------------|--------|-----|
| `python: command not found` | Python not installed/PATH | Install Python, add to PATH |
| `cannot be loaded because running scripts is disabled` | PowerShell policy | `Set-ExecutionPolicy RemoteSigned` |
| `No module named 'openai'` | Package not installed | `pip install openai` |
| `Connection error` | Wrong endpoint/network | Check Azure Portal for correct endpoint |
| `401 Unauthorized` | Wrong API key | Regenerate key in Azure Portal |
| `DeploymentNotFound` | Wrong model name | Check deployment name in Azure OpenAI Studio |
| `DNS resolution failed` | Invalid endpoint URL | Verify endpoint URL in Azure Portal |

## 📞 When All Else Fails

1. **Check the full documentation**: `documents/Lab1-Error-Solutions.md` or `documents/Lab2-Error-Solutions.md`
2. **Run diagnostic tools**: `python debug_env.py` and `python diagnostic_tool.py`
3. **Start from scratch**: Delete `venv` folder and run setup commands again
4. **Check Azure Portal**: Verify your resources are deployed and accessible

---
*Keep this handy for quick reference during lab sessions!*