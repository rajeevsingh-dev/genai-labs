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
cd genai-labs

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
Provision a multi‑service Azure AI resource and run a no‑code OCR/Read demo. → [Open Lab 1](Lab1/Readme.md)

### Lab 2: Text Generating Apps
Use Azure OpenAI from Python for basic chat & completions. → [Open Lab 2](Lab2/Readme.md)

### Lab 3: Your First ChatBot with RAG
Combine Azure AI Search retrieval with generation for a simple RAG chatbot. → [Open Lab 3](Lab3/Readme.md)

### Lab 4: Advance RAG
Enhance relevance using embeddings + hybrid search strategies. → [Open Lab 4](Lab4/README.md)

### Lab 5: RAG with a Front end API
Ship a Gradio web UI and discuss deployment considerations. → [Open Lab 5](Lab5/readme.md)

### Lab 6: Create your First Agent in AI Foundry
Build an AI Foundry agent and explore tool/function calling. → [Open Lab 6](Lab6/README.md)

## Additional Resources & Next Steps
Explore advanced agent orchestration, semantic ranking, and Responsible AI guidelines after completing the labs.

---

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

