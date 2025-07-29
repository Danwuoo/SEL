from sel.rat import SemanticRetriever


class DummyModel:
    """Simple deterministic embedding model for tests."""

    def encode(self, texts, show_progress_bar=False, convert_to_numpy=True, normalize_embeddings=True):
        import numpy as np

        vecs = np.array([[float(len(t))] for t in texts], dtype="float32")
        return vecs


def test_semantic_retriever(tmp_path):
    docs = [
        "the cat sits on the mat",
        "dogs are great pets",
        "a fish swims in its tank",
    ]
    retriever = SemanticRetriever()
    retriever.model = DummyModel()
    retriever.index_documents(docs)
    results = retriever.query("cat", top_k=1)
    assert results
    assert "cat" in results[0]["text"]

    retriever.save_index(tmp_path)
    loaded = SemanticRetriever(index_path=tmp_path)
    loaded.model = DummyModel()
    res = loaded.query("dog", top_k=1)
    assert res
    assert "dogs" in res[0]["text"]

