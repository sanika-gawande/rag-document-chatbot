from src.document_loader import load_documents, chunk_documents
from src.embeddings import create_vector_store
from src.llm_handler import LLMHandler
from src.rag_pipeline import RAGPipeline
from src.config import GEMINI_API_KEY

# Step 1: Load + chunk
docs = load_documents("./documents")
chunks = chunk_documents(docs)

# Step 2: Create vector store
vector_store = create_vector_store(chunks)

# Step 3: Setup LLM
llm_handler = LLMHandler(gemini_key=GEMINI_API_KEY)

# Step 4: Create RAG pipeline
rag = RAGPipeline(vector_store, llm_handler)

# Step 5: Ask question
query = "What is Machine Learning?"

response, sources, model = rag.query(query)

print("\nModel Used:", model)
print("\nAnswer:\n", response)

print("\nSources:\n")
for i, doc in enumerate(sources):
    print(f"{i+1}.", doc.page_content)