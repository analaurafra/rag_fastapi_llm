from rag.vector_store import similarity_search

def retrieve_context(query: str) -> str:
    docs = similarity_search(query)
    return "\n".join(docs)
