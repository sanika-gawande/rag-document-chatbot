from src.document_loader import load_documents, chunk_documents
from src.embeddings import create_vector_store, retrieve_relevant_docs

# Step 1: Load + chunk
docs = load_documents("./documents")
chunks = chunk_documents(docs)

# Step 2: Create vector DB
vector_store = create_vector_store(chunks)

# Step 3: Query
query = "What is Machine Learning?"

results = retrieve_relevant_docs(vector_store, query)

print("\nTop Results:\n")

for i, doc in enumerate(results):
    print(f"Result {i+1}:")
    print(doc.page_content)
    print("-" * 50)