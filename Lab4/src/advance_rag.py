"""
Advanced RAG Implementation
===========================
This demonstrates production-level RAG with hybrid search (keyword + vector embeddings).
See README.md for complete workshop progression and learning objectives.
"""

# Import required libraries for advanced RAG
import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery  # Key for vector search
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential

# Load configuration from .env file
load_dotenv(override=True)

# Azure AI Search configuration
AZURE_SEARCH_SERVICE = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")

# Azure OpenAI configuration
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
deployment_name = os.getenv("AZURE_OPENAI_MODEL_NAME", "gpt-4o")


# Initialize Azure services
credential = AzureKeyCredential(AZURE_SEARCH_KEY)

# Azure OpenAI client for chat completions
openai_client = AzureOpenAI(
  azure_endpoint=AZURE_OPENAI_ENDPOINT, 
  api_key=AZURE_OPENAI_API_KEY,  
  api_version="2024-02-15-preview"
)

# Azure AI Search client for hybrid search
search_client = SearchClient(
     endpoint=AZURE_SEARCH_SERVICE,
     index_name=index_name,
     credential=credential
)

# Advanced grounded prompt template for better AI responses
GROUNDED_PROMPT="""
You are an AI assistant that helps users learn from the information found in the source material.
Answer the query using only the sources provided below.
Use bullets if the answer has multiple points.
If the answer is longer than 3 sentences, provide a summary.
Answer ONLY with the facts listed in the list of sources below. Cite your source when you answer the question
If there isn't enough information below, say you don't know.
Do not generate answers that don't use the sources below.
Query: {query}
Sources:\n{sources}
"""

# Demo query for advanced RAG
#share Northwind Standard basic plan
#Share me Northwind Plan costs
query = "Share me Northwind Plan costs"

# KEY DIFFERENCE: Vector query for semantic similarity search (finds meaning, not just keywords)
vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")

# HYBRID SEARCH: Combines keyword search + vector embeddings for better results
search_results = search_client.search(
    search_text=query,              # Traditional keyword search
    vector_queries=[vector_query],  # + Semantic vector search (THIS IS THE MAGIC!)
    select=["title", "chunk"],
    top=5,
)

# Format search results for AI context
sources_formatted = "=================\n".join([
    f'TITLE: {document["title"]}, CONTENT: {document["chunk"]}' 
    for document in search_results
])

# Generate AI response using retrieved context (same as Lab3, but with better search results)
response = openai_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": GROUNDED_PROMPT.format(query=query, sources=sources_formatted)
        }
    ],
    model=deployment_name,
    temperature=0  # Consistent responses
)

# Display the advanced RAG result
print("\n" + "="*60)
print("🚀 ADVANCED RAG RESPONSE (Hybrid Search)")
print("="*60)
print(response.choices[0].message.content)
print("="*60)
print("✨ This response used BOTH keyword + vector similarity search!")

