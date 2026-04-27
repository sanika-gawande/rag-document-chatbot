from src.document_loader import load_documents, chunk_documents

docs = load_documents("./documents")
print("Documents loaded:", len(docs))

for doc in docs:
    print(doc.metadata['source'])
    print(doc.page_content[:100])
    print("------")

chunks = chunk_documents(docs)
print("Chunks created:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0].page_content)