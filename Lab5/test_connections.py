"""
Simple connection test for Lab5 RAG app
"""
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Load environment
load_dotenv(override=True)

# Get configuration
ai_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
ai_search_key = os.getenv("AZURE_SEARCH_KEY") 
ai_search_index = os.getenv("AZURE_SEARCH_INDEX_NAME")

aoai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
aoai_key = os.getenv("AZURE_OPENAI_API_KEY")
aoai_model = os.getenv("AZURE_OPENAI_MODEL_NAME")

print("🔧 Testing Connections...")
print(f"Search Endpoint: {ai_search_endpoint}")
print(f"Search Index: {ai_search_index}")
print(f"OpenAI Endpoint: {aoai_endpoint}")
print(f"OpenAI Model: {aoai_model}")
print("-" * 50)

# Test Azure AI Search
try:
    print("🔄 Testing Azure AI Search...")
    search_client = SearchClient(ai_search_endpoint, ai_search_index, AzureKeyCredential(ai_search_key))
    
    # Try a simple search
    results = list(search_client.search("test", top=1))
    print("✅ Azure AI Search connection successful!")
except Exception as e:
    print(f"❌ Azure AI Search failed: {e}")

# Test Azure OpenAI
try:
    print("🔄 Testing Azure OpenAI...")
    openai_client = AzureOpenAI(
        azure_endpoint=aoai_endpoint,
        api_key=aoai_key,
        api_version="2024-02-15-preview"
    )
    
    # Try a simple completion
    response = openai_client.chat.completions.create(
        model=aoai_model,
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=10
    )
    print("✅ Azure OpenAI connection successful!")
except Exception as e:
    print(f"❌ Azure OpenAI failed: {e}")

print("\n🎯 Connection test complete!")