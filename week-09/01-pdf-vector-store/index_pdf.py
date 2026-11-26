import os
from pathlib import Path
import time

from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from pymongo import MongoClient

from settings import COLLECTION_NAME, DB_NAME, EMBEDDING_DIMENSIONS, INDEX_NAME


def load_pdf(path: Path) -> list[Document]:
    documents = []
    for page_number, page in enumerate(PdfReader(path).pages, 1):
        text = page.extract_text()
        if text and text.strip():
            documents.append(Document(page_content=text, metadata={"source": path.name, "page": page_number}))
    return documents


def index_pdf(path: Path = Path("diabetes.pdf")) -> int:
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")
    client = MongoClient(os.environ["MONGODB_ATLAS_CLUSTER_URI"])
    collection = client[DB_NAME][COLLECTION_NAME]
    collection.delete_many({})
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2",
        google_api_key=os.environ["GEMINI_API_KEY"],
        output_dimensionality=EMBEDDING_DIMENSIONS,
    )
    store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name=INDEX_NAME,
        relevance_score_fn="cosine",
    )
    chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(load_pdf(path))
    for start in range(0, len(chunks), 50):
        store.add_documents(chunks[start:start + 50])
        if start + 50 < len(chunks):
            time.sleep(60)
    client.close()
    return len(chunks)


if __name__ == "__main__":
    print(f"Stored {index_pdf()} chunks")
