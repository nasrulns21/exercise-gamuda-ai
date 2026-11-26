import os

from settings import COLLECTION_NAME, DB_NAME, EMBEDDING_DIMENSIONS, INDEX_NAME


def create_index() -> None:
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    from langchain_mongodb import MongoDBAtlasVectorSearch
    from pymongo import MongoClient

    uri = os.environ["MONGODB_ATLAS_CLUSTER_URI"]
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2",
        google_api_key=os.environ["GEMINI_API_KEY"],
        output_dimensionality=EMBEDDING_DIMENSIONS,
    )
    client = MongoClient(uri)
    collection = client[DB_NAME][COLLECTION_NAME]
    store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name=INDEX_NAME,
        relevance_score_fn="cosine",
    )
    store.create_vector_search_index(dimensions=EMBEDDING_DIMENSIONS, wait_until_complete=60)
    client.close()


if __name__ == "__main__":
    create_index()
    print("PDF vector index created")
