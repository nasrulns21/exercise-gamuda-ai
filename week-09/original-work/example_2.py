# example_2.py: store facts in MongoDB

import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_core.documents import Document
from embeddings import embeddings

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_ATLAS_CLUSTER_URI")

client = MongoClient(MONGODB_URI)

collection = client["test_db"]["test_collection"]

# Read facts from text file
with open("facts.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

documents = []

for line in lines:
    text = line.strip()

    if text:
        documents.append(
            Document(
                page_content=text,
                metadata={"source": "facts.txt"}
            )
        )

# Connect to the existing vector store
vector_store = MongoDBAtlasVectorSearch(
    collection=collection,
    embedding=embeddings,
    index_name="test-index-1"
)

# Store documents
if documents:
    vector_store.add_documents(documents)
    print(f"Successfully added {len(documents)} documents!")
else:
    print("No documents found.")

client.close()