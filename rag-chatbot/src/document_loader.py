import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(folder_path):
    documents = []

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        if filename.endswith('.pdf'):
            loader = PyPDFLoader(filepath)

        elif filename.endswith('.txt'):
            loader = TextLoader(filepath)

        elif filename.endswith('.docx'):
            loader = Docx2txtLoader(filepath)

        else:
            continue

        documents.extend(loader.load())

    return documents


def chunk_documents(documents, chunk_size=500, overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    chunks = text_splitter.split_documents(documents)
    return chunks