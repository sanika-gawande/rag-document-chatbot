class RAGPipeline:
    def __init__(self, vector_store, llm_handler):
        self.vector_store = vector_store
        self.llm_handler = llm_handler

    def create_rag_prompt(self, query, retrieved_docs):
        """Create RAG-specific prompt"""

        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
You are a helpful AI assistant.

Use ONLY the context below to answer the question.

Context:
{context}

Question:
{query}

Instructions:
- Answer ONLY from the context
- If answer not found, say: "I don't have enough information"
- Keep answer clear and concise

Answer:
"""
        return prompt

    def query(self, user_query):
        """Execute full RAG pipeline"""

        # 1. Retrieve relevant documents
       
        docs = self.vector_store.similarity_search(user_query, k=5)

        # 2. Create prompt
        prompt = self.create_rag_prompt(user_query, docs)

        # 3. Generate response
        response, model_used = self.llm_handler.generate_response(prompt)

        return response, docs, model_used