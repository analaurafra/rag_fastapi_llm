import chromadb
from chromadb.config import Settings
from typing import List

client = chromadb.Client(Settings(persist_directory="./chroma_db"))

collection = client.get_or_create_collection(name="documents")


def add_documents(texts: List[str]):
    collection.add(documents=texts, ids=[str(i) for i in range(len(texts))])


def similarity_search(query: str, k: int = 3) -> List[str]:
    results = collection.query(query_texts=[query], n_results=k)
    # Chroma returns a dict with a "documents" key containing a list of result lists
    docs = results.get("documents", [[]])[0]
    return docs or []
