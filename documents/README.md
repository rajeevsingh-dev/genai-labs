# Gen AI Labs - Troubleshooting Documentation

This directory contains comprehensive troubleshooting guides for common issues encountered in the Gen AI Labs workshop.

## 📁 Documentation Index

### [Lab1-Error-Solutions.md](Lab1-Error-Solutions.md)
**General Setup and Environment Issues**
- Python environment configuration
- Virtual environment problems
- Package installation errors
- Azure authentication issues
- File path and directory issues
- Import and module errors

### [Lab2-Error-Solutions.md](Lab2-Error-Solutions.md)
**Azure OpenAI Connection Issues**
- Connection errors and DNS resolution failures
- Environment variable conflicts
- Authentication errors
- Model deployment issues
- Diagnostic tools and debugging methods

## 🚀 Quick Start Troubleshooting

### Most Common Issues & Quick Fixes

| Issue Category | Quick Check | Solution |
|---------------|-------------|----------|
| **Python Not Found** | `python --version` | Install Python 3.8+ or use `py` command |
| **Virtual Environment** | `.\venv\Scripts\activate` | Enable PowerShell execution policy |
| **Package Not Found** | `pip list` | `pip install -r requirements.txt` |
| **Azure Connection** | Check `.env` file | Verify endpoint URL and API key |
| **Environment Variables** | `python debug_env.py` | Use `load_dotenv(override=True)` |

### 🔧 Diagnostic Tools Available

- **`debug_env.py`** - Debug environment variable conflicts
- **`diagnostic_tool.py`** - Test Azure OpenAI connectivity
- **`setup.ps1`** - Automated environment setup script

## 📞 Getting Help

### Before Asking for Help
1. **Check the relevant error solutions document**
2. **Run the diagnostic tools**
3. **Follow the troubleshooting checklists**
4. **Try the quick fixes above**

### When Reporting Issues
Include the following information:
- **Operating System**: Windows/macOS/Linux version
- **Python Version**: Output of `python --version`
- **Lab Number**: Which lab you're working on
- **Error Message**: Full error text
- **Steps Taken**: What you've already tried
- **Environment**: Output of diagnostic tools

## 📚 Additional Resources

### Microsoft Documentation
- [Azure OpenAI Service](https://docs.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure CLI Documentation](https://docs.microsoft.com/en-us/cli/azure/)
- [Python Azure SDK](https://docs.microsoft.com/en-us/azure/developer/python/)

### Python Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [pip Documentation](https://pip.pypa.io/en/stable/)

### PowerShell Resources
- [PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
- [Execution Policy Guide](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy)

## 🔄 Document Updates

This documentation is based on real troubleshooting sessions and will be updated as new issues are discovered and resolved.

**Last Updated**: November 8, 2025
**Version**: 1.0

---

## 📋 Lab-Specific Quick Links

### Lab1 Issues
- [Python Environment Setup](Lab1-Error-Solutions.md#python-environment-issues)
- [Virtual Environment Problems](Lab1-Error-Solutions.md#virtual-environment-problems)
- [Package Installation](Lab1-Error-Solutions.md#package-installation-errors)

### Lab2 Issues  
- [Azure OpenAI Connection](Lab2-Error-Solutions.md#connection-error---dns-resolution-failed)
- [Environment Variable Conflicts](Lab2-Error-Solutions.md#environment-variable-conflicts)
- [Authentication Problems](Lab2-Error-Solutions.md#authentication-errors)

---

*These documents are living resources - if you encounter new issues or find better solutions, please contribute to keep them updated!*