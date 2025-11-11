# Lab2 - Azure OpenAI Demos

This lab provides **two progressive demos** showing how to connect to Azure OpenAI using Python with key-based authentication. 
Start with the basic demo and progress through more advanced features.

## Prerequisites

1. **Azure OpenAI Resource**: You need an Azure OpenAI resource deployed in your Azure subscription
2. **Model Deployment**: Deploy a chat model (e.g., GPT-3.5-turbo or GPT-4) in your Azure OpenAI resource
3. **API Access**: Obtain your endpoint URL and API key from the Azure portal

## Setup Instructions

### 1. Set up Virtual Environment

```powershell
cd Lab2
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Configure Environment Variables

1. Copy the `example.env` file to `.env`
2. Update the following values in your `.env` file:

```env
# Your Azure OpenAI resource endpoint
AZURE_OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com

# Your Azure OpenAI API key (Key 1 or Key 2 from Azure portal)
AZURE_OPENAI_API_KEY=your_api_key_here

# Your model deployment name
AZURE_OPENAI_MODEL_NAME=gpt-4o
```

### 4. Run the Demos

### Demo Files
- `azure_openai_demo1.py` - **Basic demo** - Simple connection with static question
- `azure_openai_demo2.py` - **Interactive demo** - Q&A chat with error handling  

**Choose your learning level:**

#### 🌱 Demo 1: Basic Connection (Perfect for First-Time Users)
```powershell
python azure_openai_demo1.py
```
- **Static Question**: Asks "What is artificial intelligence?"
- **No User Input**: Runs automatically and exits
- **Perfect for**: Quick demonstrations and understanding basics

#### 🚀 Demo 2: Interactive Chat (Learning Experience)  
```powershell
python azure_openai_demo2.py
```
- **Interactive**: Ask multiple questions in a chat format
- **Error Handling**: Helpful error messages and diagnostics
- **User-Friendly**: Clean interface with guidance
- **Perfect for**: Learning how interactive AI chat works


## 📁 Project Structure

```
Lab2/
├── ReadMe.md                    # This file - Lab instructions
├── azure_openai_demo1.py        # Basic demo - Simple connection
├── azure_openai_demo2.py        # Interactive demo - Q&A chat
├── requirements.txt             # Python dependencies
├── example.env                  # Template for environment variables
└── .env                        # Your actual configuration (create this)
```


### Configuration & Setup
- `requirements.txt` - Python dependencies
- `example.env` - Template for environment variables
- `.env` - Your actual configuration (create from example.env)

## Demo Examples

### 🌱 Basic Demo Output (`azure_openai_demo1.py`)
```
🤖 Connecting to Azure OpenAI...
❓ Question: What is artificial intelligence?
🤔 Getting response...

💡 Answer: Artificial Intelligence (AI) refers to the simulation of human intelligence in machines...

✅ Demo completed successfully!

Next steps:
- Try changing the question in the code
- Run azure_openai_demo.py for an interactive version
```

### 🚀 Interactive Demo Output (`azure_openai_demo2.py`)
```
🤖 Azure OpenAI Demo - Simple Q&A Chat
==================================================
✅ Successfully connected to Azure OpenAI!
Using model deployment: gpt-4o

You can now ask questions! Type 'quit' or 'exit' to end the session.

🙋 Your question: What is artificial intelligence?
🤔 Thinking...

🤖 Azure OpenAI: Artificial Intelligence (AI) refers to the simulation of human intelligence...

--------------------------------------------------
🙋 Your question: quit
👋 Goodbye! Thanks for using Azure OpenAI demo.
```


## Reference Documentation

- [Azure OpenAI Service Documentation](https://docs.microsoft.com/en-us/azure/ai-services/openai/)
- [Azure OpenAI Python SDK](https://docs.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line&pivots=programming-language-python)
- [Azure OpenAI Authentication](https://docs.microsoft.com/en-us/azure/ai-services/openai/how-to/authentication)


## ✅ Lab2 Success Criteria

You've successfully completed Lab2 when you can:
- [x] Run all three demos without errors
- [x] Understand the progression from basic to advanced features
- [x] Connect to your Azure OpenAI resource successfully
- [x] Ask questions and receive AI responses

## ➡️ Next Steps

Once you've completed all tasks and verified your setup, proceed to:
- **[Lab 3: Your First ChatBot with RAG](../Lab3/Readme.md)** - Learn to build RAG-powered chatbots!

---

**🎉 Congratulations on completing Lab 2!** 
You now understand Azure OpenAI basics and are ready for more advanced scenarios.