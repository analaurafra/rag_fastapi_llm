from rag.loader import load_documents


def test_load_documents_returns_list_of_strings():
    docs = load_documents()
    assert isinstance(docs, list)
    assert len(docs) > 0
    assert all(isinstance(d, str) for d in docs)
