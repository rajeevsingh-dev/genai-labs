






# Lab 6: Create your First Agent in AI Foundry

Welcome to Lab 6! In this lab, you'll explore Azure AI Foundry Agent Service and build your first AI agent with tool calling capabilities.

## 🎯 Lab Objectives

By the end of this lab, you will:
- Understand what AI agents are and when to use them
- Learn the difference between agents and chatbots
- Create agents using Azure AI Foundry Portal (no-code)
- Build agents programmatically with Python SDK
- Implement tool calling (Code Interpreter)
- Explore multi-agent workflows
- Understand Semantic Kernel integration for advanced scenarios

## 📋 Prerequisites

- Completed Lab 1-5 (Azure AI foundations and RAG)
- Azure subscription with AI Foundry access
- Python 3.8+ installed
- Azure CLI authenticated (`az login`)
- Basic understanding of Azure OpenAI

## 🚀 Getting Started

### 1. Set Up Environment

```powershell
cd Lab6
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and update:

```env
# Azure AI Foundry Project Configuration
AZURE_AI_PROJECT_ENDPOINT=https://your-project.api.azureml.ms
AZURE_AI_MODEL_DEPLOYMENT=gpt-4o

# Optional: For advanced scenarios
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
```

### 3. Authenticate with Azure

```powershell
az login
```

### 4. Run the Quickstart Agent

```powershell
python src/quickstart-agent.py
```

**Expected Output:**
```
Created agent, ID: asst_abc123
Created thread, ID: thread_xyz789
Created message, ID: msg_001
Run finished with status: completed

Role: assistant, Content: [Graph visualization response]
Role: user, Content: Hi, Agent! Draw a graph for a line...

Saved image file to: abc123_image_file.png
```

---

## 📁 Project Structure

```
Lab6/
├── README.md                    # This file - Lab instructions
├── src/
│   └── quickstart-agent.py     # Basic agent creation with Code Interpreter
├── requirements.txt             # Python dependencies
├── .env.example                # Template for environment variables
├── .env                        # Your credentials (create this)
└── venv/                       # Virtual environment (created)
```

---

## 🤖 What is an Agent?

**AI Agents** are autonomous systems that can:
- Use tools and functions to take actions
- Make decisions based on context
- Execute multi-step workflows
- Interact with external systems
- Remember conversation state across interactions

### Agent vs. Chatbot

| Feature | Chatbot (Labs 2-5) | AI Agent (Lab 6) |
|---------|-------------------|------------------|
| **Purpose** | Answer questions | Take actions |
| **Capability** | Text responses | Tool calling, function execution |
| **Autonomy** | Reactive | Proactive decision-making |
| **Memory** | Conversation history | Persistent threads and state |
| **Tools** | None | Code Interpreter, Functions, APIs |
| **Example Use** | Customer support | Data analysis, automation |

---

## 🛠️ Azure AI Foundry Agent Options

Azure offers several ways to create agents:

### 1. **Azure AI Foundry Agents (Recommended for Enterprise)**
- Managed, enterprise-ready platform
- Portal-based (no-code) and SDK (code-first)
- Built-in governance, monitoring, scalability
- **Best for**: Production scenarios

### 2. **Semantic Kernel Agent Framework**
- Open-source SDK for custom agents
- Maximum flexibility and extensibility
- **Best for**: Custom orchestration, complex workflows

### 3. **Microsoft Agent Framework (Preview)**
- Unified framework across Microsoft platforms
- Integration with Copilot and other services
- **Best for**: Latest unified agent tools

### 4. **Other Options**
- Azure Bot Service (conversational bots)
- Power Virtual Agents (low-code)
- Custom solutions with Azure Functions

---

## 📖 Lab Walkthrough

### Understanding the Quickstart Code

The `quickstart-agent.py` demonstrates:

**1. Agent Creation**
```python
agent = project_client.agents.create_agent(
    model="gpt-4o",
    name="my-agent1",
    instructions="You help with math and visualization",
    tools=code_interpreter.definitions  # Enable Code Interpreter
)
```

**2. Thread Creation**
```python
thread = project_client.agents.threads.create()
```

**3. Message and Run**
```python
message = project_client.agents.messages.create(
    thread_id=thread.id,
    role="user",
    content="Draw a graph with slope 4 and y-intercept 9"
)

run = project_client.agents.runs.create_and_process(
    thread_id=thread.id,
    agent_id=agent.id
)
```

**4. Retrieve Results**
```python
messages = project_client.agents.messages.list(thread_id=thread.id)
for message in messages:
    print(f"Role: {message.role}, Content: {message.content}")
```

---

## 🧪 Try Different Scenarios

Modify the code to test different agent capabilities:

### Scenario 1: Data Analysis
```python
content="Analyze this dataset: [1,2,3,4,5,10,15,20]. Find mean, median, and create a histogram."
```

### Scenario 2: Code Generation
```python
content="Write Python code to calculate Fibonacci sequence up to 100"
```

### Scenario 3: Math Problem Solving
```python
content="Solve the quadratic equation: x² + 5x + 6 = 0"
```


## ✅ Lab Completion Checklist

- [ ] Set up Python environment and dependencies
- [ ] Configured Azure AI Foundry credentials
- [ ] Successfully authenticated with Azure CLI
- [ ] Ran `quickstart-agent.py` successfully
- [ ] Agent created and executed code
- [ ] Image file generated and saved
- [ ] Understood agent vs. chatbot differences
- [ ] Explored Code Interpreter tool capabilities
- [ ] Reviewed different agent creation options

---

## 🆘 Troubleshooting

**Issue**: "AZURE_AI_PROJECT_ENDPOINT not found"
- **Solution**: Ensure `.env` file exists and has correct endpoint
- Get endpoint from Azure AI Foundry portal → Project settings

**Issue**: Authentication failed
- **Solution**: Run `az login` and ensure correct subscription is selected
- Check that you have permissions to Azure AI Foundry

**Issue**: Model deployment not found
- **Solution**: Verify `AZURE_AI_MODEL_DEPLOYMENT` matches your deployed model name in AI Foundry

**Issue**: Agent run fails
- **Solution**: Check agent instructions are clear
- Verify Code Interpreter tool is properly configured
- Review run error details in output

---

## 🎓 What You Learned

- AI agents enable autonomous actions beyond simple Q&A
- Azure AI Foundry provides managed agent services
- Code Interpreter tool allows agents to write and execute code
- Threads maintain conversation state persistently
- Multiple agent creation approaches for different needs
- Production-ready agent patterns with Azure

---

## 📚 Additional Resources

### Official Documentation
- [Azure AI Foundry Overview](https://learn.microsoft.com/azure/ai-foundry/)
- [What is an Agent?](https://learn.microsoft.com/azure/ai-foundry/agents/overview)
- [Semantic Kernel Agent Framework](https://learn.microsoft.com/semantic-kernel/frameworks/agent/)
- [Microsoft Agent Framework](https://learn.microsoft.com/microsoft-copilot-studio/microsoft-agent-framework)

### Tools and Services
- [Azure Bot Service](https://azure.microsoft.com/services/bot-service/)
- [Power Virtual Agents](https://powervirtualagents.microsoft.com/)

---

## ➡️ Next Steps

**Continue your agent journey:**
- Explore tool calling with custom functions
- Build multi-agent workflows
- Integrate with Semantic Kernel for advanced orchestration
- Deploy agents to production with enterprise governance

---

**🎉 Congratulations on creating your first AI Agent!**

You've completed all 6 labs and built a comprehensive understanding of GenAI from basics to production-ready applications and intelligent agents. 🚀


Get started : https://learn.microsoft.com/en-us/azure/ai-foundry/

