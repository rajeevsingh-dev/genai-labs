# Interactive Simple RAG (Retrieval Augmented Generation)
# =======================================================
# This code demonstrates how RAG works in three simple steps:
# 1. Search: Find relevant documents
# 2. Retrieve: Get the content from those documents  
# 3. Generate: Use AI to create an answer based on the retrieved content
#
# This version allows users to ask MULTIPLE questions interactively

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Load environment variables
load_dotenv(override=True)

# Step 1: Set up our connections to Azure Services
# --------------------------------------------

# Initialize Azure AI Search
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

# Initialize Azure OpenAI
openai_client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# Step 2: Define our helper functions
# --------------------------------------------

def search_documents(user_question, top_k=3):
    """
    Search for relevant documents in Azure AI Search
    This is the 'Retrieval' part of RAG
    """
    print(f"\n🔍 Searching for relevant documents about: '{user_question}'")
    
    # Search the index for relevant documents
    results = search_client.search(
        search_text=user_question,
        select=["title", "chunk"],  # We want the content and source file
        top=top_k  # Get top 3 most relevant documents
    )
    
    # Collect all the relevant content
    documents = []
    for result in results:
        documents.append(
            f"Content: {result['chunk']}\n"
            f"Source: {result['title']}\n"
        )
    
    return "\n".join(documents)

def generate_answer(user_question, relevant_content):
    """
    Generate an answer using Azure OpenAI
    This is the 'Generation' part of RAG
    """
    print("🤖 Generating answer based on retrieved content...")
    
    # Create a prompt that tells the AI how to respond
    system_prompt = """
    You are a helpful assistant that answers questions based on the provided documents.
    - Use ONLY the information from the provided sources
    - If the answer is not in the sources, say "I don't have enough information to answer that"
    - Use bullet points for multiple items
    - Always cite your source
    """
    
    # Combine everything the AI needs to know
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"""
        Please answer this question: {user_question}
        
        Here are the relevant documents to use:
        {relevant_content}
        """}
    ]
    
    # Get the AI's response
    response = openai_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_MODEL_NAME", "gpt-4o"),  # Use model from .env
        messages=messages,
        temperature=0  # Make it consistent
    )
    
    return response.choices[0].message.content

# Step 3: Interactive Main Program
# --------------------------------

def main():
    print("🎯 Interactive Simple RAG!")
    print("=" * 50)
    print("Ask questions about the Northwind Benefits documents")
    print("Type 'exit' to quit")
    print()
    
    question_count = 0
    
    while True:
        # Get the user's question
        question = input("❓ What's your question? ")
        
        if question.lower() in ['exit', 'quit', 'bye']:
            print("👋 Goodbye!")
            break
        
        question_count += 1
        print(f"\n--- Question #{question_count} ---")
        
        try:
            # Step 1: Search for relevant content
            relevant_content = search_documents(question)
            
            # Step 2: Generate an answer using the content
            answer = generate_answer(question, relevant_content)
            
            # Step 3: Show the answer
            print("\n🎯 Answer:")
            print("=" * 30)
            print(answer)
            print("=" * 30)
            print()
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print()

if __name__ == "__main__":
    main()