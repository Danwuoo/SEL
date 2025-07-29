"""Semantic retrieval utilities for RAT."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import faiss
from sentence_transformers import SentenceTransformer

from .utils import embed_batch


class SemanticRetriever:
    """Retrieve relevant document chunks using a vector index."""

    def __init__(self, index_path: str | None = None, encoder_model: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        self.model = SentenceTransformer(encoder_model)
        self.index: Optional[faiss.Index] = None
        self.docstore: List[str] = []
        self.metadata: List[dict] = []
        if index_path:
            self.load_index(index_path)

    def _ensure_index(self, dim: int) -> None:
        if self.index is None:
            self.index = faiss.IndexFlatIP(dim)

    def index_documents(self, documents: List[str], metadata: Optional[List[dict]] = None) -> None:
        """Add ``documents`` to the index with optional ``metadata``."""

        embeddings = embed_batch(self.model, documents)
        self._ensure_index(embeddings.shape[1])
        self.index.add(embeddings)
        self.docstore.extend(documents)
        if metadata is None:
            metadata = [{} for _ in documents]
        self.metadata.extend(metadata)

    def query(self, query: str, top_k: int = 5) -> List[Dict]:
        """Return top-``k`` matching documents and metadata."""

        if self.index is None or self.index.ntotal == 0:
            return []
        query_emb = embed_batch(self.model, [query])
        _, indices = self.index.search(query_emb, top_k)
        results = []
        for idx in indices[0]:
            if idx == -1:
                continue
            results.append({"text": self.docstore[idx], "metadata": self.metadata[idx]})
        return results

    def save_index(self, output_path: str) -> None:
        """Persist index and metadata under ``output_path``."""

        path = Path(output_path)
        path.mkdir(parents=True, exist_ok=True)
        if self.index is not None:
            faiss.write_index(self.index, str(path / "index.faiss"))
        with open(path / "store.json", "w", encoding="utf-8") as f:
            json.dump({"documents": self.docstore, "metadata": self.metadata}, f)

    def load_index(self, path: str) -> None:
        """Load index and metadata from ``path``."""

        base = Path(path)
        self.index = faiss.read_index(str(base / "index.faiss"))
        with open(base / "store.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        self.docstore = data["documents"]
        self.metadata = data["metadata"]
