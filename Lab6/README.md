






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

---

## 🎓 Learning Path

This lab is structured in two parts:

### Part 1: AI Foundry Agent Service (Current Lab)
1. ✅ **Lab #1**: Environment Setup  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/environment-setup)

2. ✅ **Lab #2**: Create Agent using Portal (No-code)  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/quickstart?pivots=ai-foundry-portal)

3. ✅ **Lab #3**: Agents with Tool Calling  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/overview)

4. ✅ **Lab #4**: Create Agents using Python SDK (This Lab)  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/quickstart?pivots=programming-language-python-azure)

5. **Lab #5**: Enterprise Features  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/use-your-own-resources)

6. **Lab #6**: Multi-agent Workflows (Portal)  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/connected-agents?pivots=portal)

7. **Lab #7**: Multi-agent Workflows (Python)  
   [Guide](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/connected-agents?pivots=python)

8. **Lab #8**: Getting Started with Processes  
   [Guide](https://learn.microsoft.com/semantic-kernel/frameworks/process/examples/example-human-in-loop?pivots=programming-language-python)

### Part 2: Custom Agents with Semantic Kernel
9. **Lab #9**: Building Custom Agents using Semantic Kernel  
   [Guide](https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python)

---

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


What is an Agent?

Various options for creating an Agent?

Azure offers several options for creating agents, each suited for different scenarios and levels of abstraction:
1. Azure AI Foundry Agents (via azure-ai-projects):

Provides a managed, enterprise-ready platform for building, deploying, and managing AI agents.
Supports both portal-based and code-first (Python SDK) approaches.
Best for production scenarios, enterprise integration, and when you want built-in governance, monitoring, and scalability.
Overview
2. Semantic Kernel Agent Framework:

An open-source SDK for building custom AI agents and workflows using plugins, planners, and connectors.
Offers flexibility and extensibility for developers who want to deeply customize agent logic and orchestration.
Integrates with Azure OpenAI and other LLMs.
Semantic Kernel Agent Framework
3. Microsoft Agent Framework (Public Preview):

A new, unified framework for building, composing, and deploying agents, aiming to standardize agent development across Microsoft platforms.
Designed for extensibility and integration with Microsoft Copilot and other services.
Agent Framework Overview
Other Options in the Microsoft Ecosystem:

Azure Bot Service: For conversational bots (chatbots, voice bots) with integration to Teams, Web Chat, etc. Azure Bot Service
Power Virtual Agents: Low-code/no-code platform for building conversational agents, especially for business users. Power Virtual Agents
Custom Solutions: You can also build agents using Azure Functions, Logic Apps, or custom code with Azure OpenAI, depending on your requirements.
How to Choose:

Use AI Foundry Agents for managed, scalable, and enterprise-grade agent solutions.
Use Semantic Kernel for maximum flexibility and custom orchestration.
Try the Agent Framework if you want to leverage the latest unified agent development tools (currently in preview).
Use Bot Service or Power Virtual Agents for conversational interfaces and business process automation.


What is Azure AI Foundry Agent Services?
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview


![alt text](image.png)


![alt text](agent.png)

Why Use Azure AI Foundry Agent Service?






Labs: will be divided in two parts:

Part1: Create Agents using AI foundry Agent Service using Foundry Portal and Python

Part2: Create Custom Agents suing AI Foundry Services and Orchestartion Layer, Semantic Kernal.

Here’s a comparison of default agent creation using Azure AI Foundry Agent Service versus creating agents with Semantic Kernel integration:

Default Agent Creation with Azure AI Foundry Agent Service

When you create a new project in the Azure AI Foundry portal, a default agent is automatically provisioned for you.
You can immediately interact with this agent in the Agents Playground by providing instructions and chatting with it.
The default agent uses the GPT-4o model (or your selected deployment) and can be customized with instructions and knowledge files.
This approach is fast, requires no code, and is ideal for quick prototyping or business users.
You can later enhance the agent by adding tools, files, or connecting it to external data sources.
See: Quickstart: Create a new agent (portal) and Get started with Azure AI Foundry
Agent Creation with Azure AI Foundry Agent Service + Semantic Kernel

You can create and manage agents programmatically using the Azure AI Foundry Python SDK or C# SDK, and then integrate them with the Semantic Kernel Agent Framework.
This approach allows you to leverage Semantic Kernel’s advanced orchestration, plugin, and planner capabilities, enabling more complex workflows and custom logic.
You configure the agent’s endpoint and deployment in your Semantic Kernel code, then interact with the agent using the Semantic Kernel abstractions.
This method is best for developers who want to build extensible, multi-agent, or tool-augmented solutions, and integrate with other AI services or plugins.
See: Exploring the Semantic Kernel AzureAIAgent and Develop an AI agent with Semantic Kernel
Summary Table

Approach	No-Code Portal	SDK/Code	Extensibility	Tool/Plugin Support	Best For
Default Agent (Portal)	Yes	No	Basic	Limited	Fast prototyping, business use
Agent with Semantic Kernel Integration	No	Yes	Advanced	Extensive	Developers, custom workflows
References:

Quickstart: Create a new agent (portal)
Quickstart: Create a new agent (Python SDK)
Semantic Kernel AzureAIAgent
Develop an AI agent with Semantic Kernel


Part1 labs:

Lab#1: Environment Set up
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/environment-setup


Lab#2: Quickstart: Create Agent using AI Foundry Portal
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/quickstart?pivots=ai-foundry-portal

Lab#3: Agents with Tools calling
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/overview

Lab#4: Create Agents using azure-ai-projects and Python
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/quickstart?pivots=programming-language-python-azure

Lab#5: Exploring Enterprise features
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/use-your-own-resources

Lab#6: Create Multi-agent workflows: Connected agents using AI Foundry portal
[Hand off thread context to other agents to focus on specialised tasks]
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/connected-agents?pivots=portal

Lab#7: Create Multi-agent workflows: Connected agents using Python
https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/connected-agents?pivots=python

Lab#8: Getting started with Process
https://github.com/microsoft/semantic-kernel/tree/main/python/samples/getting_started_with_processes
https://learn.microsoft.com/en-us/semantic-kernel/frameworks/process/examples/example-human-in-loop?pivots=programming-language-python

---------------------------------------
Lab9# Building Custom Agents using Semantic Kernel Agent Framework
https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/?pivots=programming-language-python
