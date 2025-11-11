# Azure OpenAI Demo Files - Usage Guide

This folder contains three different versions of Azure OpenAI demos, each designed for different learning stages and use cases.

## 📁 File Overview

### 1. `azure_openai_demo1.py` - **Basic Demo** 🌱
**Perfect for: First-time users, quick demonstration**

**What it does:**
- Connects to Azure OpenAI
- Asks one predefined question: "What is artificial intelligence?"
- Shows the response
- Exits automatically

**Features:**
- ✅ Minimal code (less than 40 lines)
- ✅ No user input required
- ✅ Static demonstration
- ✅ Perfect for understanding the basics

**To run:**
```powershell
python azure_openai_demo1.py
```

### 2. `azure_openai_demo.py` - **Interactive Demo** 🚀
**Perfect for: Learning interactive AI chat, basic troubleshooting**

**What it does:**
- Interactive Q&A session
- Users can ask multiple questions
- Basic error handling and diagnostics
- Clean exit options

**Features:**
- ✅ Interactive chat loop
- ✅ Error handling with helpful messages
- ✅ Configuration debugging
- ✅ Connection validation

**To run:**
```powershell
python azure_openai_demo.py
```

### 3. `azure_openai_demo2.py` - **Enhanced Demo** ⭐
**Perfect for: Advanced users, feature exploration, production-like experience**

**What it does:**
- Full-featured chat application
- Multiple conversation modes
- Conversation history and management
- Usage statistics and performance metrics

**Features:**
- ✅ **3 Conversation Modes:**
  - 🤖 Assistant (balanced)
  - 🎨 Creative (imaginative)  
  - 🔬 Precise (factual)
- ✅ **Conversation Management:**
  - View chat history
  - Save conversations to JSON
  - Clear conversation
- ✅ **Advanced Stats:**
  - Token usage tracking
  - Response time measurement
  - Session statistics
- ✅ **Enhanced Commands:**
  - `mode` - Switch conversation style
  - `history` - View conversation
  - `save` - Export chat
  - `clear` - Start fresh
  - `stats` - Usage statistics

**To run:**
```powershell
python azure_openai_demo2.py
```

## 🎯 Which Demo Should You Use?

### For Teaching/Workshops:
1. **Start with Demo 1** - Show the absolute basics
2. **Move to Demo** - Interactive experience  
3. **Explore Demo 2** - Advanced features

### For Different Audiences:
- **Executives/Decision Makers**: Demo 1 (quick, impressive)
- **Developers/Technical Users**: Demo (practical, interactive)
- **Power Users/Advanced Developers**: Demo 2 (full features)

### For Troubleshooting:
- **Connection Issues**: Use Demo (has diagnostic info)
- **Environment Problems**: All demos will help identify issues
- **Feature Testing**: Demo 2 (comprehensive testing)

## 📋 Prerequisites (All Demos)

1. **Python Environment:**
   ```powershell
   python --version  # Should be 3.8+
   ```

2. **Virtual Environment:**
   ```powershell
   .\venv\Scripts\activate
   ```

3. **Dependencies Installed:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configuration File:**
   - Ensure `.env` file exists with correct values
   - Check `example.env` for template

## 🚀 Quick Start Guide

### Step 1: Choose Your Demo Level
```powershell
# Basic (static demo)
python azure_openai_demo1.py

# Interactive (Q&A chat)
python azure_openai_demo.py  

# Enhanced (full features)
python azure_openai_demo2.py
```

### Step 2: Configuration Check
If any demo fails, run the diagnostic:
```powershell
python debug_env.py
python diagnostic_tool.py
```

## 🔧 Demo 2 Special Commands Reference

When running `azure_openai_demo2.py`, you can use these special commands:

| Command | Description | Example |
|---------|-------------|---------|
| `mode` | Switch conversation style | Changes AI personality |
| `history` | View all messages | See your chat history |
| `save` | Export conversation | Saves to JSON file |
| `clear` | Start fresh | Clears conversation |
| `stats` | Usage statistics | Shows tokens, time, etc. |
| `quit` / `exit` | End session | Exits with save option |

## 📊 Sample Demo 2 Session

```
🤖 Azure OpenAI Demo 2 - Enhanced Q&A Chat
=======================================================
✅ Successfully connected to Azure OpenAI!
Using model deployment: gpt-4o

🎭 Conversation Modes:
   1. 🤖 Assistant - You are a helpful assistant
   2. 🎨 Creative - You are a creative and imaginative assistant  
   3. 🔬 Precise - You are a precise and factual assistant

🤖 Your message: Tell me about space exploration
🤔 Thinking...

🤖 Azure OpenAI (Assistant mode): Space exploration represents humanity's quest to understand and explore the cosmos beyond Earth...

📈 Response stats: 156 tokens | 2.34s
-------------------------------------------------------
🤖 Your message: mode
Choose mode (1-3): 2
✅ Switched to 🎨 Creative mode

🎨 Your message: Tell me about space exploration
🤔 Thinking...

🎨 Azure OpenAI (Creative mode): Imagine space as an infinite ocean of stars, where each mission is like sending a bottle with humanity's dreams across cosmic waves...

📈 Response stats: 203 tokens | 3.12s  
-------------------------------------------------------
🎨 Your message: stats

📊 Session Statistics:
   💬 Messages: 4
   🎯 Current mode: 🎨 Creative
   🔢 Total tokens used: 359
```

## 🆘 Need Help?

- **Setup Issues**: Check `documents/Lab2-Error-Solutions.md`
- **Connection Problems**: Run `python diagnostic_tool.py`
- **Environment Issues**: Check `documents/Lab1-Error-Solutions.md`  
- **Quick Reference**: See `documents/Quick-Reference.md`

---

*Choose the demo that matches your experience level and gradually progress through all three for a complete learning experience!*