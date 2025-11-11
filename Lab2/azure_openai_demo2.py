"""
Azure OpenAI Demo - Simple Q&A Chat
====================================

This demo shows how to connect to Azure OpenAI using Python with key-based authentication.
Users can ask questions and receive responses from Azure OpenAI.

Prerequisites:
- Azure OpenAI resource deployed in Azure
- A deployed model (e.g., GPT-3.5-turbo or GPT-4)
- Azure OpenAI endpoint and API key

Reference: https://docs.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line&pivots=programming-language-python
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load environment variables from .env file (override system env vars)
load_dotenv(override=True)

def initialize_azure_openai():
    """
    Initialize Azure OpenAI client with key-based authentication
    
    Returns:
        AzureOpenAI: Configured Azure OpenAI client
    """
    try:
        # Get configuration from environment
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
        
        # Debug: Print configuration (hide most of the API key for security)
        print(f"🔧 Configuration:")
        print(f"   Endpoint: {endpoint}")
        print(f"   API Key: {api_key[:10]}...{api_key[-5:] if api_key else 'None'}")
        print(f"   API Version: {api_version}")
        
        # Check if required values are present
        if not endpoint:
            print("❌ AZURE_OPENAI_ENDPOINT not found in environment variables")
            return None
        if not api_key:
            print("❌ AZURE_OPENAI_API_KEY not found in environment variables")
            return None
            
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version
        )
        print("✅ Successfully connected to Azure OpenAI!")
        return client
    except Exception as e:
        print(f"❌ Failed to initialize Azure OpenAI: {str(e)}")
        return None

def ask_question(client, question, model_deployment_name):
    """
    Send a question to Azure OpenAI and get a response
    
    Args:
        client (AzureOpenAI): Azure OpenAI client
        question (str): User's question
        model_deployment_name (str): Name of your deployed model
        
    Returns:
        str: AI response or error message
    """
    try:
        print(f"🔧 Using model deployment: {model_deployment_name}")
        
        response = client.chat.completions.create(
            model=model_deployment_name,  # Your model deployment name (e.g., "gpt-35-turbo")
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide clear and concise answers."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,  # Controls randomness (0-1)
            max_tokens=500,   # Maximum length of response
            top_p=0.95        # Controls diversity of response
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        error_msg = str(e)
        if "DeploymentNotFound" in error_msg:
            return f"❌ Model deployment '{model_deployment_name}' not found. Please check your model deployment name in Azure OpenAI Studio."
        elif "Unauthorized" in error_msg:
            return f"❌ Authentication failed. Please check your API key."
        elif "Connection" in error_msg:
            return f"❌ Connection error: {error_msg}. Please check your endpoint URL and internet connection."
        else:
            return f"❌ Error getting response: {error_msg}"

def main():
    """
    Main function to run the Azure OpenAI demo
    """
    print("🤖 Azure OpenAI Demo - Simple Q&A Chat")
    print("=" * 50)
    
    # Initialize Azure OpenAI client
    client = initialize_azure_openai()
    
    if not client:
        print("Please check your Azure OpenAI configuration and try again.")
        return
    
    # Get model deployment name from environment or use default
    model_name = os.getenv("AZURE_OPENAI_MODEL_NAME", "gpt-4o")
    print(f"Using model deployment: {model_name}")
    
    print("\nYou can now ask questions! Type 'quit' or 'exit' to end the session.\n")
    
    # Chat loop
    while True:
        try:
            # Get user input
            user_question = input("🙋 Your question: ").strip()
            
            # Check for exit commands
            if user_question.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye! Thanks for using Azure OpenAI demo.")
                break
            
            # Skip empty questions
            if not user_question:
                print("Please enter a question.")
                continue
            
            # Get AI response
            print("🤔 Thinking...")
            response = ask_question(client, user_question, model_name)
            
            # Display response
            print(f"\n🤖 Azure OpenAI: {response}\n")
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()