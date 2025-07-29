"""Semantic retrieval utilities for RAT."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np


class SemanticRetriever:
    """Very simple lexical retriever for tests."""

    def __init__(self, index_path: Optional[str] = None, encoder_model: str | None = None) -> None:
        self.docstore: List[str] = []
        self.metadata: List[dict] = []
        if index_path:
            self.load_index(index_path)

    def index_documents(self, documents: List[str], metadata: Optional[List[dict]] = None) -> None:
        if not documents:
            return
        self.docstore.extend(documents)
        if metadata is None:
            metadata = [{} for _ in documents]
        self.metadata.extend(metadata)

    def _score(self, query: str, doc: str) -> float:
        q_tokens = set(query.lower().split())
        d_tokens = set(doc.lower().split())
        return len(q_tokens & d_tokens)

    def query(self, query_text: str, top_k: int = 5) -> List[Dict]:
        if not self.docstore:
            return []
        scores = np.array([self._score(query_text, d) for d in self.docstore], dtype=float)
        indices = np.argsort(-scores)[:top_k]
        results = []
        for idx in indices:
            if scores[idx] <= 0:
                continue
            results.append({"text": self.docstore[idx], "metadata": self.metadata[idx], "score": float(scores[idx])})
        return results

    def save_index(self, output_path: str) -> None:
        path = Path(output_path)
        path.mkdir(parents=True, exist_ok=True)
        with open(path / "store.json", "w", encoding="utf-8") as f:
            json.dump({"documents": self.docstore, "metadata": self.metadata}, f, indent=2)

    def load_index(self, path: str) -> None:
        base = Path(path)
        store_file = base / "store.json"
        if not store_file.exists():
            raise FileNotFoundError(f"Index files not found in {path}")
        with open(store_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.docstore = data["documents"]
        self.metadata = data["metadata"]
