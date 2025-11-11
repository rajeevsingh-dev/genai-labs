"""
Simple RAG with Gradio UI
========================
Basic RAG: User Query → Search Documents → AI Response
"""

import os
from dotenv import load_dotenv
import gradio as gr
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.models import VectorizedQuery

load_dotenv()

# Configuration
ai_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
ai_search_key = os.getenv("AZURE_SEARCH_KEY")
ai_search_index = os.getenv("AZURE_SEARCH_INDEX_NAME")
aoai_deployment = os.getenv("AZURE_OPENAI_MODEL_NAME")
aoai_key = os.getenv("AZURE_OPENAI_API_KEY")
aoai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
aoai_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
aoai_embedding_model = os.getenv("AZURE_OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")

# Initialize clients
chat_client = AzureOpenAI(
    api_version=aoai_api_version,
    api_key=aoai_key,
    azure_endpoint=aoai_endpoint
)

embedding_client = AzureOpenAI(
    api_version=aoai_api_version,
    api_key=aoai_key,
    azure_endpoint=aoai_endpoint
)

search_client = SearchClient(ai_search_endpoint, ai_search_index, AzureKeyCredential(ai_search_key))

def search_and_respond(user_query):
    """Simple RAG: Search + Generate Response"""
    try:
        # 1. Generate embeddings for user query
        query_vector = embedding_client.embeddings.create(
            input=user_query,
            model=aoai_embedding_model
        ).data[0].embedding
        
        # 2. Search for relevant documents
        vector_query = VectorizedQuery(
            vector=query_vector,
            k_nearest_neighbors=5,
            fields="text_vector"
        )
        
        search_results = list(search_client.search(
            search_text=user_query,
            vector_queries=[vector_query],
            select=["chunk", "title"],
            top=3
        ))
        
        # 3. Format context from search results
        context = ""
        for doc in search_results:
            context += f"Title: {doc['title']}\nContent: {doc['chunk']}\n\n"
        
        # 4. Generate AI response
        messages = [
            {"role": "system", "content": f"Answer the user's question based on this context:\n\n{context}"},
            {"role": "user", "content": user_query}
        ]
        
        response = chat_client.chat.completions.create(
            model=aoai_deployment,
            messages=messages,
            temperature=0.3,
            max_tokens=200
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        # Simple demo response when Azure is unavailable
        return f"""🤖 **Northwind Benefits Assistant** (Demo Mode)

I apologize, but I'm currently unable to connect to Azure services to search through the documents.

For your question: "{user_query}"

In a real scenario, I would:
1. Search through Northwind benefits documents
2. Find relevant information 
3. Provide a detailed answer based on the documents

**Example topics I can help with:**
• Health insurance coverage
• Retirement plans and 401(k)
• Paid time off policies  
• Professional development benefits
• Life insurance options

*[Demo Mode - Azure connection unavailable]*"""

def chat_function(message, history):
    """Simple chat function for Gradio interface."""
    return search_and_respond(message)

if __name__ == "__main__":
    print("🚀 Starting Simple RAG Chatbot...")
    
    # Create Gradio interface
    demo = gr.ChatInterface(
        fn=chat_function,
        title="Northwind RAG Chatbot 🏢",
        description="Ask me about Northwind's benefits!",
        examples=[
            "What are the benefits offered?",
            "Tell me about healthcare coverage",
            "What is the Northwind Standard plan?"
        ]
    )
    
    # Launch the app
    demo.launch(server_port=7862, inbrowser=True)
