# Lab2 - Azure OpenAI Error Solutions

This document captures common errors and troubleshooting solutions encountered when working with Azure OpenAI in Lab2.

## Table of Contents
1. [Connection Error - DNS Resolution Failed](#connection-error---dns-resolution-failed)
2. [Environment Variable Conflicts](#environment-variable-conflicts)
3. [Authentication Errors](#authentication-errors)
4. [Model Deployment Issues](#model-deployment-issues)
5. [General Troubleshooting Steps](#general-troubleshooting-steps)
6. [Diagnostic Tools](#diagnostic-tools)

---

## Connection Error - DNS Resolution Failed

### Error Message
```
❌ Error getting response: Connection error.
```

### Detailed Error (from diagnostic)
```
❌ Connection error: HTTPSConnectionPool(host='chat-with-your-data-azure-openai-demo.openai.azure.com', port=443): Max retries exceeded with url: /openai/deployments?api-version=2024-02-15-preview (Caused by NameResolutionError: Failed to resolve 'chat-with-your-data-azure-openai-demo.openai.azure.com')
```

### Root Cause
- **DNS Resolution Failure**: The endpoint URL cannot be resolved by DNS
- **Incorrect Endpoint**: The endpoint URL doesn't exist or is misconfigured

### Solution Steps
1. **Verify Endpoint URL in Azure Portal**
   - Navigate to [Azure Portal](https://portal.azure.com)
   - Go to your Azure OpenAI resource
   - Click "Keys and Endpoint" in the left menu
   - Copy the exact **Endpoint** value

2. **Update Configuration**
   - Ensure the endpoint URL is correct in your `.env` file
   - Format should be: `https://your-resource-name.openai.azure.com/`

---

## Environment Variable Conflicts

### Error Symptoms
- Configuration shows different values than what's in `.env` file
- System environment variables override `.env` file values

### Root Cause Analysis
Our diagnostic revealed:
```
📁 Before loading .env file:
AZURE_OPENAI_ENDPOINT: https://chat-with-your-data-azure-openai-demo.openai.azure.com/

📁 After loading .env file:
AZURE_OPENAI_ENDPOINT: https://chat-with-your-data-azure-openai-demo.openai.azure.com/

📖 Contents of .env file:
AZURE_OPENAI_ENDPOINT=https://genai-azure-open-ai.openai.azure.com/
```

**Issue**: System environment variables take precedence over `.env` file values.

### Solutions

#### Solution 1: Clear System Environment Variables (Temporary)
```powershell
# Clear for current session
$env:AZURE_OPENAI_ENDPOINT = $null
$env:AZURE_OPENAI_API_KEY = $null
```

#### Solution 2: Force .env Override (Code Fix)
Update your Python code to override system environment variables:
```python
# Change this:
load_dotenv()

# To this:
load_dotenv(override=True)
```

#### Solution 3: Clear System Environment Variables (Permanent)
**Windows:**
1. Open "Environment Variables" from System Properties
2. Remove `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY` from both User and System variables

**PowerShell (Session only):**
```powershell
Remove-Item Env:AZURE_OPENAI_ENDPOINT -ErrorAction SilentlyContinue
Remove-Item Env:AZURE_OPENAI_API_KEY -ErrorAction SilentlyContinue
```

---

## Authentication Errors

### Error Messages
```
❌ HTTP Error 401: Unauthorized
❌ Authentication failed - check your API key
```

### Troubleshooting Steps
1. **Verify API Key**
   - Go to Azure Portal → Azure OpenAI resource → "Keys and Endpoint"
   - Copy Key 1 or Key 2 (both work equally)
   - Ensure no extra spaces or characters

2. **Check API Key Format**
   - Should be 32+ characters long
   - Contains alphanumeric characters
   - No quotes or special characters around it in `.env` file

3. **Regenerate API Key**
   - If key doesn't work, regenerate it in Azure Portal
   - Update `.env` file with new key

---

## Model Deployment Issues

### Error Messages
```
❌ Model deployment 'gpt-4o' not found
❌ DeploymentNotFound: The API deployment for this resource does not exist
```

### Solutions
1. **Check Model Deployment Name**
   - Go to Azure OpenAI Studio or Azure Portal
   - Navigate to "Model deployments"
   - Use the exact **Deployment name** (not the model name)

2. **Common Model Deployment Names**
   ```
   gpt-35-turbo     (for GPT-3.5 Turbo)
   gpt-4            (for GPT-4)
   gpt-4o           (for GPT-4o)
   text-embedding-ada-002  (for embeddings)
   ```

3. **Deploy Model if Missing**
   - In Azure OpenAI Studio, go to "Deployments"
   - Click "Create new deployment"
   - Select model and give it a deployment name
   - Update your `.env` file with the deployment name

---

## General Troubleshooting Steps

### Step 1: Environment Setup Verification
```powershell
# Ensure you're in the right directory
cd C:\MyREPO\Workshop\gen-ai-labs\Lab2

# Activate virtual environment
.\venv\Scripts\activate

# Install/upgrade dependencies
pip install -r requirements.txt
```

### Step 2: Configuration Check
```python
# Run the debug script we created
python debug_env.py
```

### Step 3: Connection Test
```python
# Run the diagnostic tool
python diagnostic_tool.py
```

### Step 4: Manual Verification
1. **Test endpoint in browser**: Visit your endpoint URL (should show OpenAI API documentation)
2. **Ping test**: `ping your-resource-name.openai.azure.com`
3. **Network check**: Ensure no firewall/proxy blocking Azure domains

---

## Diagnostic Tools

We created several diagnostic tools during troubleshooting:

### 1. Environment Debug Tool (`debug_env.py`)
**Purpose**: Shows environment variable conflicts
```python
python debug_env.py
```
**What it shows**:
- Environment variables before/after loading .env
- Contents of .env file
- Current working directory

### 2. Connection Diagnostic Tool (`diagnostic_tool.py`)
**Purpose**: Tests actual Azure OpenAI connectivity
```python
python diagnostic_tool.py
```
**What it tests**:
- Basic endpoint connectivity
- Authentication
- Available model deployments
- Network connectivity

### 3. Enhanced Demo with Debug Info (`azure_openai_demo.py`)
**Features**:
- Shows configuration being used
- Detailed error messages
- Model deployment validation

---

## Quick Resolution Checklist

When encountering Azure OpenAI connection issues, check these in order:

- [ ] **Internet connectivity** - Can you browse other websites?
- [ ] **Correct directory** - Are you in the Lab2 folder?
- [ ] **Virtual environment** - Is it activated? (`.\venv\Scripts\activate`)
- [ ] **Dependencies installed** - Run `pip install -r requirements.txt`
- [ ] **Environment variables** - Run `python debug_env.py` to check conflicts
- [ ] **Endpoint URL** - Verify in Azure Portal (Keys and Endpoint section)
- [ ] **API Key** - Verify in Azure Portal (try regenerating if needed)
- [ ] **Model deployment** - Check deployment name in Azure OpenAI Studio
- [ ] **Network/Firewall** - Run `python diagnostic_tool.py`

---

## Common Configuration Template

Here's a working `.env` template:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_KEY=your-32-character-api-key-here
AZURE_OPENAI_MODEL_NAME=gpt-35-turbo
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

**Important Notes**:
- Replace `your-resource-name` with your actual Azure OpenAI resource name
- Replace `your-32-character-api-key-here` with your actual API key
- Use your actual model deployment name for `AZURE_OPENAI_MODEL_NAME`
- Keep the trailing slash `/` in the endpoint URL

---

## Support Resources

- **Azure OpenAI Documentation**: https://docs.microsoft.com/en-us/azure/ai-services/openai/
- **Python SDK Documentation**: https://github.com/openai/openai-python
- **Azure OpenAI Quickstart**: https://docs.microsoft.com/en-us/azure/ai-services/openai/quickstart
- **Azure OpenAI Authentication**: https://docs.microsoft.com/en-us/azure/ai-services/openai/how-to/authentication