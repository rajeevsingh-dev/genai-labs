"""
Azure OpenAI Demo 1 - Basic Connection
=====================================

This is the simplest possible demonstration of connecting to Azure OpenAI.
Perfect for first-time users to understand the basics.

What this demo does:
1. Connects to Azure OpenAI
2. Sends a single question 
3. Gets and displays the response

Prerequisites:
- Azure OpenAI resource with a deployed model
- .env file with your credentials

Reference: https://docs.microsoft.com/en-us/azure/ai-services/openai/quickstart
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load your configuration from .env file
load_dotenv()

# Step 1: Set up connection to Azure OpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview"
)

# Step 2: Ask a question
question = "What is artificial intelligence?"

print("🤖 Connecting to Azure OpenAI...")
print(f"❓ Question: {question}")
print("🤔 Getting response...")

# Step 3: Get response from Azure OpenAI
response = client.chat.completions.create(
    model="gpt-4o",  # Your model deployment name
    messages=[
        {"role": "user", "content": question}
    ],
    max_tokens=200
)

# Step 4: Display the answer
answer = response.choices[0].message.content
print(f"\n💡 Answer: {answer}")

print("\n✅ Demo completed successfully!")
print("\nNext steps:")
print("- Try changing the question in the code")
print("- Run azure_openai_demo2.py for an interactive version")