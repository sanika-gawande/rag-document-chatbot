# 🤖 RAG Chatbot

## 📌 Overview

A terminal-based chatbot that answers questions using custom documents via Retrieval-Augmented Generation (RAG).

---

## 📂 Supported Files

Place documents inside `documents/` folder:

* `.txt` ✅
* `.docx` ✅
* `.pdf` ⚠️ (text-based only)

> Note: Convert scanned PDFs to `.txt` for best results.

---

## ⚙️Setup Instructions
1. Install dependencies
pip install -r requirements.txt
2. Install Ollama (Local LLM)

Download: https://ollama.com/

ollama pull phi3
3. (Optional) Gemini Setup

Create .env file:

GEMINI_API_KEY=your_api_key_here

▶️ Run the Chatbot
python -m src.chatbot

💬 Example Queries

Ask questions based on your documents:
What are the advantages of blockchain?
What challenges are faced in AI systems?
Explain supervised and unsupervised learning.
Compare Machine Learning and Blockchain.
🚨 4. Edge Case Questions.
What is quantum computing?
Explain space technology.

Commands:

* `exit` → quit
* `clear` → clear chat
* `help` → show commands
* `status` → system info

---

## 🧠 How it Works

```text
Query → FAISS Search → Context → LLM → Answer
```

---

## 📁 Structure

```text
rag-chatbot/
├── documents/
├── src/
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── llm_handler.py
│   ├── rag_pipeline.py
│   └── chatbot.py
```

---

## ⚡ Tech Stack

* Python
* LangChain
* FAISS
* Ollama (Local LLM)

---

## 👩‍💻 Author

Sanika Gawande
