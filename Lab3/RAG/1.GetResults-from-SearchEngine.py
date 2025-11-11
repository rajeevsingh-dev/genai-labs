
# Step 1: Import Required Libraries
# ===================================
import os
from dotenv import load_dotenv  # For loading environment variables from .env file
from azure.search.documents import SearchClient  # Azure AI Search client for performing searches
from azure.search.documents.models import VectorizableTextQuery  # For creating vector-based queries
from azure.core.credentials import AzureKeyCredential  # For authenticating with Azure services

# Step 2: Load Configuration from Environment File
# ==============================================
# Load environment variables from .env file to keep sensitive info secure
load_dotenv()

# Get Azure AI Search configuration from environment variables
# These values should be set in your .env file
AZURE_SEARCH_SERVICE = os.getenv("AZURE_SEARCH_ENDPOINT")  # Your Azure AI Search service URL
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")  # Your Azure AI Search admin key
index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")  # Name of the search index to query

# Step 3: Validate Configuration
# =============================
# Check if all required configuration values are loaded properly
print(f"Search Service: {AZURE_SEARCH_SERVICE}")
print(f"Search Key: {'Found' if AZURE_SEARCH_KEY else 'Missing'}")
print(f"Index Name: {index_name}")

# Exit if essential configuration is missing
if not AZURE_SEARCH_KEY:
    print("❌ AZURE_SEARCH_KEY is missing from .env file")
    exit(1)

# Step 4: Create Authentication Credential
# ======================================
# Create credential object using the API key for Azure AI Search authentication
credential = AzureKeyCredential(AZURE_SEARCH_KEY)

# Step 5: Define Search Query
# ==========================
# This is the question/text we want to find relevant documents for
query = "Share Northwind Standard is a basic plan"  

# Step 6: Create Search Client
# ===========================
# Initialize the Azure AI Search client to connect to your search service
search_client = SearchClient(endpoint=AZURE_SEARCH_SERVICE, credential=credential, index_name=index_name)

# Step 7: Create Vector Query
# ==========================
# Create a vector query that converts text to embeddings and finds similar documents
# k_nearest_neighbors=50: Find top 50 most similar documents
# fields="text_vector": Search in the vector field that contains document embeddings
vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
  
# Step 8: Perform Hybrid Search
# =============================
# Execute both text search and vector search to find the most relevant documents
# search_text=query: Traditional keyword-based search
# vector_queries=[vector_query]: Semantic/meaning-based search using embeddings
# select=["chunk"]: Only return the 'chunk' field from matching documents
# top=1: Return only the most relevant result
results = search_client.search(  
    search_text=query,  
    vector_queries=[vector_query],
    select=["chunk"],
    top=1
)  

# Step 9: Display Search Results
# =============================
# Loop through the results and display the relevance score and document content
for result in results:  
    print(f"Score: {result['@search.score']}")  # Relevance score (higher = more relevant)
    print(f"Chunk: {result['chunk']}")  # The actual text content that matched our query