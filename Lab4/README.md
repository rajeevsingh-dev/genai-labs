# 🚀 Lab4: Advanced RAG (Retrieval-Augmented Generation)

## 📚 Workshop Progression Recap

### 🎯 Lab2: Azure OpenAI Foundations
**What we learned:**
- ✅ Basic Azure OpenAI connections and authentication
- ✅ Simple chat completions with static responses  
- ✅ Environment variable management
- ✅ Progressive demo complexity (basic → interactive → enhanced)

### 🎯 Lab3: Simple RAG Implementation
**What we learned:**
- ✅ Basic RAG concepts: **Retrieval** → **Augmentation** → **Generation**
- ✅ Simple keyword-based document search
- ✅ Basic prompt engineering for grounded responses
- ✅ Interactive vs. hardcoded question patterns

---

## 🚀 Lab4: Advanced RAG - What We're Building Now

### Why We Need Advanced RAG ?

**Problem with Simple Keyword Search:**
- Misses semantic meaning and context
- **Example:** User asks about "benefits" but document uses "advantages" or "perks"
- Same concept, different words = missed results
- Limited to exact word matches

**Solution: Vector Embeddings + Hybrid Search**
- Understands meaning and context, not just keywords
- Finds semantically similar content even with different words
- Combines best of keyword matching + semantic understanding

---

### 🔍 Advanced Features We're Implementing

#### 1. **Hybrid Search (Keyword + Vector Embeddings)**
```python
# ADVANCED HYBRID SEARCH
vector_query = VectorizableTextQuery(
    text=user_question, 
    k_nearest_neighbors=50, 
    fields="text_vector"
)

results = search_client.search(
    search_text=user_question,        # Keyword search
    vector_queries=[vector_query],    # + Semantic search
    select=["title", "chunk"],
    top=5
)
```

#### 2. **Advanced Prompt Engineering**
- Sophisticated grounded prompt templates
- Better instruction clarity for AI responses  
- Enhanced source citation and formatting

#### 3. **Production-Ready Patterns**
- Error handling and validation
- Configurable parameters (top_k, temperature, etc.)
- Scalable architecture for real applications

---

### 📊 Simple RAG vs Advanced RAG Comparison

| Feature | Lab3 Simple RAG | Lab4 Advanced RAG |
|---------|-----------------|-------------------|
| **Search Type** | Keyword only | Hybrid (Keyword + Vector) |
| **Semantic Understanding** | ❌ No | ✅ Yes |
| **Synonym Handling** | ❌ Limited | ✅ Excellent |
| **Context Awareness** | ❌ Basic | ✅ Advanced |
| **Prompt Engineering** | ⭐ Simple | ⭐⭐⭐ Sophisticated |
| **Production Ready** | ❌ Demo only | ✅ Enterprise ready |

---

### 🎯 Real-World Impact

**What this means for your applications:**
- 🎯 **More accurate document retrieval** - finds relevant content even with different terminology
- 🧠 **Better semantic understanding** - understands user intent, not just keywords
- ⚡ **Higher quality responses** - AI gets better context to work with
- 🏢 **Enterprise-ready RAG** - production-level techniques used in real AI applications

---

## � Getting Started

### Prerequisites

- Completed Lab 3 (Simple RAG)
- Azure OpenAI resource with deployed models
- Azure AI Search service with indexed documents (with vector fields)
- Python 3.8+ installed

### Setup Instructions

#### 1. Install Dependencies

```powershell
cd Lab4
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 2. Configure Environment Variables

Copy `example.env` to `.env` and update with your credentials:

```env
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_MODEL_NAME=gpt-4o

# Azure AI Search Configuration
AZURE_SEARCH_ENDPOINT=https://your-search.search.windows.net
AZURE_SEARCH_KEY=your_search_key_here
AZURE_SEARCH_INDEX_NAME=your-index-name

# API Version
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

#### 3. Run the Advanced RAG Demo

```powershell
python src/advance_rag.py
```

**Expected Output:**
```
============================================================
🚀 ADVANCED RAG RESPONSE (Hybrid Search)
============================================================
Based on the Northwind plans:

- **Northwind Basic**: $50/month
- **Northwind Standard**: $120/month  
- **Northwind Plus**: $200/month

Sources: Northwind Benefits Overview
============================================================
✨ This response used BOTH keyword + vector similarity search!
```

### Try Different Queries

Edit the `query` variable in `src/advance_rag.py` to test different questions:

```python
# Example queries to try:
query = "Share me Northwind Plan costs"  # Current query
query = "What benefits does Standard plan offer?"
query = "Compare Basic and Plus plans"
query = "Tell me about health insurance coverage"
```

---

## 📁 Project Structure

```
Lab4/
├── README.md              # This file - Lab instructions and concepts
├── src/
│   └── advance_rag.py    # Advanced RAG implementation with hybrid search
├── requirements.txt       # Python dependencies
├── example.env           # Template for environment variables
└── .env                  # Your credentials (create this)
```

---

## 🔍 Code Walkthrough

### Key Implementation Details

**1. Vector Query Creation**
```python
vector_query = VectorizableTextQuery(
    text=query, 
    k_nearest_neighbors=50,  # Find top 50 similar documents
    fields="text_vector"      # Search in vector embeddings field
)
```

**2. Hybrid Search Execution**
```python
search_results = search_client.search(
    search_text=query,              # Keyword search
    vector_queries=[vector_query],  # + Vector search
    select=["title", "chunk"],
    top=5  # Return top 5 results
)
```

**3. Advanced Prompt Engineering**
```python
GROUNDED_PROMPT = """
You are an AI assistant that helps users learn from source material.
Answer using only the sources provided below.
Use bullets if the answer has multiple points.
Cite your source when you answer the question.
If there isn't enough information, say you don't know.

Query: {query}
Sources:\n{sources}
"""
```

---

## ✅ Lab Completion Checklist

- [ ] Understood limitations of keyword-only search
- [ ] Learned about vector embeddings and semantic search
- [ ] Configured environment with Azure credentials
- [ ] Successfully ran `advance_rag.py`
- [ ] Tested multiple queries and observed results
- [ ] Compared responses with Lab 3 simple RAG
- [ ] Understood hybrid search benefits

---

## 🎓 What You Learned

- Vector embeddings enable semantic understanding beyond keywords
- Hybrid search combines the best of keyword matching and semantic similarity
- Advanced prompt engineering improves response quality and consistency
- Production RAG requires proper error handling and configuration management
- k-nearest neighbors (KNN) search finds semantically similar content

---

## 📚 Additional Resources

- [Azure AI Search Vector Search Documentation](https://learn.microsoft.com/azure/search/vector-search-overview)
- [Hybrid Search in Azure AI Search](https://learn.microsoft.com/azure/search/hybrid-search-overview)
- [RAG Performance Best Practices](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag-solution-design-and-evaluation-guide)

---

## ➡️ Next Steps

Ready to build a production-ready RAG application with a web interface?
- **[Lab 5: RAG with a Front end API](../Lab5/readme.md)** - Create a Gradio-based chatbot with deployment capabilities!

---

**🎉 Congratulations on mastering Advanced RAG with hybrid search!**

### 🚀 What You'll Learn in Lab4

1. **Vector Embeddings** - How AI understands meaning beyond keywords
2. **Hybrid Search** - Combining multiple search strategies for better results  
3. **Advanced Prompting** - Production-level prompt engineering techniques
4. **Performance Optimization** - Making RAG fast and scalable
5. **Error Handling** - Building robust, production-ready RAG systems

---

### 📖 Prerequisites

Before starting Lab4, ensure you've completed:
- ✅ Lab2: Azure OpenAI basics
- ✅ Lab3: Simple RAG implementation
- ✅ Understanding of basic RAG workflow

---

### 🎓 Learning Objectives

By the end of Lab4, you will:
- Understand the limitations of keyword-only search
- Implement hybrid search combining keywords and vector embeddings  
- Create production-ready RAG systems with proper error handling
- Apply advanced prompt engineering techniques for better AI responses
- Build scalable RAG architectures suitable for enterprise applications

**Let's build some advanced RAG magic! 🎯✨**