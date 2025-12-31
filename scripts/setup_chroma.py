from rag.loader import load_documents
from rag.vector_store import collection


def populate_collection():
    docs = load_documents()
    if not docs:
        print("No documents to add.")
        return

    # Try to compute a start offset based on existing ids to avoid duplicates
    try:
        existing = collection.get(include=["ids"]) or {}
        existing_ids = existing.get("ids", [])
        start = len(existing_ids)
    except Exception:
        start = 0

    ids = [str(i + start) for i in range(len(docs))]
    collection.add(documents=docs, ids=ids)
    print(f"Added {len(docs)} documents starting at id {start}.")


if __name__ == "__main__":
    populate_collection()
