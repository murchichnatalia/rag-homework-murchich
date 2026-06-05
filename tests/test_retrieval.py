from app.retriever import Retriever


def test_retriever_loads():
    retriever = Retriever()
    assert retriever is not None


def test_retrieval_returns_results():
    retriever = Retriever()
    results = retriever.search("crime TV shows")

    assert len(results) > 0