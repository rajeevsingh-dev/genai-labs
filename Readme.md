# GenAI for Beginners — Hands-on Workshop

A two-day hands-on workshop focused on Generative AI with a practical emphasis on Retrieval-Augmented Generation (RAG) and AI Agents. This repository contains lab descriptions, quick-start instructions, and guidance to help beginners learn by doing.

---

## Table of Contents

- [Audience](#audience)
- [Duration](#duration)
- [Workshop Objectives](#workshop-objectives)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Workshop Structure](#workshop-structure)
  - [Day 1: Azure AI Foundations & RAG Basics](#day-1-azure-ai-foundations--rag-basics)
  - [Day 2: Advanced RAG & AI Agents](#day-2-advanced-rag--ai-agents)
- [Labs Overview](#labs-overview)
  - [Lab 1: Create your First Azure AI Service](#lab-1-create-your-first-azure-ai-service)
  - [Lab 2: Text Generating Apps](#lab-2-text-generating-apps)
  - [Lab 3: Your First ChatBot with RAG](#lab-3-your-first-chatbot-with-rag)
  - [Lab 4: Advance RAG](#lab-4-advance-rag)
  - [Lab 5: RAG with a Front end API](#lab-5-rag-with-a-front-end-api)
  - [Lab 6: Create your First Agent in AI Foundry](#lab-6-create-your-first-agent-in-ai-foundry)
- [Additional Resources & Next Steps](#additional-resources--next-steps)
- [Feedback and Contribution](#feedback-and-contribution)

---

## Audience

- Beginners to Generative AI and RAG
- Developers, data engineers, and solution architects seeking practical, hands-on experience
- Anyone interested in building AI-powered applications with Azure

## Duration

**Recommended:** 2 days (3 labs per day)
- **Day 1:** Azure AI Foundations & RAG Basics (Lab 1-3)
- **Day 2:** Advanced RAG & AI Agents (Lab 4-6)

## Workshop Objectives

By the end of this workshop participants will be able to:

- Create and configure Azure AI services (Azure OpenAI, Azure AI Search)
- Build text-generating applications using Azure OpenAI
- Understand and implement RAG (Retrieval-Augmented Generation) concepts
- Develop chatbots with document retrieval capabilities
- Create production-ready RAG applications with web interfaces
- Build and deploy AI agents using Azure AI Foundry

## Prerequisites

- Python 3.8 or higher
- An active Azure subscription with permissions to create resources
- Azure CLI installed and authenticated (`az login`)
- Visual Studio Code (recommended extensions: Azure Account, Azure CLI Tools, Python)
- Git for cloning the repository
- Basic familiarity with Python and command line

**Checklist:**

- [ ] Azure subscription
- [ ] Azure CLI installed and logged in
- [ ] Python 3.8+ installed
- [ ] VS Code installed
- [ ] Git installed

## Quick Start

```powershell
# Clone the repository
git clone <repo-url>
cd gen-ai-labs

# Open in VS Code
code .
```

Each lab folder contains an `example.env` file. Copy it to `.env` and update with your Azure credentials before running the code.

---

## Workshop Structure

### Day 1: Azure AI Foundations & RAG Basics

**Focus:** Setting up Azure AI services and understanding basic RAG concepts

| Lab | Title | Duration | Focus |
|-----|-------|----------|-------|
| Lab 1 | Create your First Azure AI Service | 60-90 min | Azure setup & configuration |
| Lab 2 | Text Generating Apps | 60-90 min | Azure OpenAI basics |
| Lab 3 | Your First ChatBot with RAG | 90-120 min | Simple RAG implementation |

### Day 2: Advanced RAG & AI Agents

**Focus:** Production-ready RAG applications and AI agent development

| Lab | Title | Duration | Focus |
|-----|-------|----------|-------|
| Lab 4 | Advance RAG | 90-120 min | Hybrid search & vector embeddings |
| Lab 5 | RAG with a Front end API | 90-120 min | Web UI & deployment |
| Lab 6 | Create your First Agent in AI Foundry | 90-120 min | AI agents & tool calling |

---

## Labs Overview

### Lab 1: Create your First Azure AI Service

**Goal:** Set up Azure OpenAI and Azure AI Search services, and verify connectivity.

**What you'll learn:**
- Create Azure OpenAI resource via Azure Portal
- Deploy GPT models and embedding models
- Create Azure AI Search service
- Configure environment variables
- Test Azure OpenAI connection using Python SDK

**Key Outputs:**
- Working Azure OpenAI resource
- Deployed chat and embedding models
- Azure AI Search service ready for indexing

📂 **Location:** [Lab1/ReadMe.md](Lab1/ReadMe.md)

*Estimated time: 60–90 minutes*

---

### Lab 2: Text Generating Apps

**Goal:** Build interactive text-generating applications using Azure OpenAI.

**What you'll learn:**
- Connect to Azure OpenAI using Python SDK
- Implement key-based authentication
- Create basic chat completion applications
- Build interactive Q&A chatbots
- Handle errors and implement best practices

**Key Outputs:**
- Basic demo with static questions
- Interactive chat application
- Understanding of Azure OpenAI SDK patterns

**Demos included:**
- `azure_openai_demo1.py` - Basic connection demo
- `azure_openai_demo2.py` - Interactive Q&A chat

📂 **Location:** [Lab2/Readme.md](Lab2/Readme.md)

*Estimated time: 60–90 minutes*

---

### Lab 3: Your First ChatBot with RAG

**Goal:** Implement a basic RAG pipeline that retrieves documents and generates contextual responses.

**What you'll learn:**
- Understand RAG concepts: Retrieval → Augmentation → Generation
- Connect to Azure AI Search
- Implement keyword-based document retrieval
- Combine retrieved context with LLM generation
- Add source citations to responses

**Key Outputs:**
- Search engine integration
- Simple RAG implementation
- Interactive RAG chatbot

**Scripts included:**
- `1.GetResults-from-SearchEngine.py` - Search foundation
- `2.simple_rag.py` - Basic RAG demo
- `3.simple_rag_interactive.py` - Interactive RAG

📂 **Location:** [Lab3/Readme.md](Lab3/Readme.md)

*Estimated time: 90–120 minutes*

---

### Lab 4: Advance RAG

**Goal:** Implement production-grade RAG with hybrid search and vector embeddings.

**What you'll learn:**
- Limitations of keyword-only search
- Vector embeddings and semantic search
- Hybrid search (keyword + vector)
- Advanced prompt engineering
- Production-ready error handling

**Key Concepts:**
- Semantic understanding vs. keyword matching
- k-nearest neighbors (KNN) vector search
- Combining multiple search strategies
- Performance optimization

📂 **Location:** [Lab4/README.md](Lab4/README.md)

*Estimated time: 90–120 minutes*

---

### Lab 5: RAG with a Front end API

**Goal:** Build a production-ready RAG application with Gradio web interface.

**What you'll learn:**
- Create web-based chat interfaces with Gradio
- Implement conversation history tracking
- Add citation tracking and source attribution
- Deploy to Azure App Service
- Production readiness and best practices

**Key Features:**
- Interactive Gradio web UI
- Real-time chat responses
- Source citation display
- Azure deployment guide

**Topics covered:**
- Production readiness
- Sample architectures
- AI landing zones
- Deployment strategies

📂 **Location:** [Lab5/readme.md](Lab5/readme.md)

*Estimated time: 90–120 minutes*

---

### Lab 6: Create your First Agent in AI Foundry

**Goal:** Build and deploy AI agents using Azure AI Foundry Agent Service.

**What you'll learn:**
- What are AI agents and when to use them
- Azure AI Foundry Agent Service overview
- Create agents using the Foundry Portal
- Build agents programmatically with Python SDK
- Implement tool calling and connected agents
- Explore Semantic Kernel integration

**Key Topics:**
- Agent vs. chatbot differences
- Tool integration (Code Interpreter, Functions)
- Multi-agent workflows
- Enterprise features and governance

**Implementation approaches:**
- Portal-based agent creation (no-code)
- Python SDK for programmatic control
- Semantic Kernel for advanced orchestration

📂 **Location:** [Lab6/README.md](Lab6/README.md)

*Estimated time: 90–120 minutes*

---

## Additional Resources & Next Steps

### Documentation
- Each lab folder contains detailed `README.md` with step-by-step instructions
- `example.env` files in each lab show required configuration
- Error solutions available in `documents/` folder

### Sample Data
- Sample documents in `Lab-Data/` folder
- Pre-configured for Northwind Benefits scenario

### Next Steps
- Explore advanced agent scenarios with Semantic Kernel
- Implement custom tools and plugins
- Build multi-agent systems
- Deploy to production with Azure App Service

## Feedback and Contribution

Please open issues or submit pull requests to suggest improvements, corrections, or additional labs.

---

## License

This project is licensed under the MIT License. That means you can:

- Use the code for personal, educational, or commercial projects
- Modify and distribute it
- Keep attribution by retaining the original copyright notice

Limitations and responsibilities:
- The software is provided "as is" without warranty of any kind
- Authors are not liable for any damages resulting from its use

See the full license text in the [`LICENSE`](LICENSE) file.

---

**Happy learning — build responsibly and enjoy exploring GenAI and Azure AI!** 🚀

