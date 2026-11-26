import os

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from pymongo import MongoClient

from rag_service import Chunk, RagService


def build_live_service() -> RagService:
    client = MongoClient(os.environ["MONGODB_ATLAS_CLUSTER_URI"])
    collection = client["test_db"]["test_collection_pdf"]
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2",
        google_api_key=os.environ["GEMINI_API_KEY"],
        output_dimensionality=768,
    )
    store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name="test-index-pdf",
        relevance_score_fn="cosine",
    )
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ["GEMINI_API_KEY"])

    def retrieve(question: str) -> list[Chunk]:
        documents = store.similarity_search(question, k=4)
        return [Chunk(document.page_content, int(document.metadata.get("page", 0))) for document in documents]

    def answer(question: str, chunks: list[Chunk]) -> str:
        context = "\n\n".join(f"Page {chunk.page}: {chunk.text}" for chunk in chunks)
        prompt = f"Answer only from the context. If the answer is absent, say so.\n\nContext:\n{context}\n\nQuestion: {question}"
        return llm.invoke(prompt).text

    return RagService(retrieve, answer)
