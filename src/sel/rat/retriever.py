"""Semantic retrieval utilities for RAT."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import faiss
from sentence_transformers import SentenceTransformer

from .utils import embed_batch


class SemanticRetriever:
    """
    Retrieve relevant document chunks using a vector index.

    This class provides a simple interface to:
    - Index a corpus of documents.
    - Query the index for the most similar documents.
    - Save and load the index from disk.
    """

    def __init__(
        self,
        index_path: Optional[str] = None,
        encoder_model: str = "sentence-transformers/all-MiniLM-L6-v2",
    ) -> None:
        """
        Initialize the retriever.

        Args:
            index_path: Optional path to a pre-built index.
            encoder_model: The name of the sentence-transformer model to use.
        """
        self.model = SentenceTransformer(encoder_model)
        self.index: Optional[faiss.Index] = None
        self.docstore: List[str] = []
        self.metadata: List[dict] = []
        if index_path:
            self.load_index(index_path)

    def _ensure_index(self, dim: int) -> None:
        """Create a FAISS index if one doesn't already exist."""
        if self.index is None:
            # Using IndexFlatIP for cosine similarity with normalized embeddings
            self.index = faiss.IndexFlatIP(dim)

    def index_documents(
        self, documents: List[str], metadata: Optional[List[dict]] = None
    ) -> None:
        """
        Index a list of documents.

        Args:
            documents: The documents to index.
            metadata: Optional metadata for each document.
        """
        if not documents:
            return

        embeddings = embed_batch(self.model, documents)
        self._ensure_index(embeddings.shape[1])
        self.index.add(embeddings)
        self.docstore.extend(documents)

        if metadata is None:
            metadata = [{} for _ in documents]
        self.metadata.extend(metadata)

    def query(self, query_text: str, top_k: int = 5) -> List[Dict]:
        """
        Query the index for the most similar documents.

        Args:
            query_text: The text to search for.
            top_k: The number of results to return.

        Returns:
            A list of dictionaries, each containing the document text and metadata.
        """
        if self.index is None or self.index.ntotal == 0:
            return []

        query_embedding = embed_batch(self.model, [query_text])
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx == -1:
                continue
            results.append(
                {
                    "text": self.docstore[idx],
                    "metadata": self.metadata[idx],
                    "score": distances[0][i].item(),
                }
            )
        return results

    def save_index(self, output_path: str) -> None:
        """
        Save the index and document store to disk.

        Args:
            output_path: The directory to save the index to.
        """
        path = Path(output_path)
        path.mkdir(parents=True, exist_ok=True)

        if self.index:
            faiss.write_index(self.index, str(path / "index.faiss"))

        with open(path / "store.json", "w", encoding="utf-8") as f:
            json.dump(
                {"documents": self.docstore, "metadata": self.metadata},
                f,
                indent=2,
            )

    def load_index(self, path: str) -> None:
        """
        Load an index from disk.

        Args:
            path: The directory containing the index files.
        """
        base = Path(path)
        index_file = base / "index.faiss"
        store_file = base / "store.json"

        if not index_file.exists() or not store_file.exists():
            raise FileNotFoundError(f"Index files not found in {path}")

        self.index = faiss.read_index(str(index_file))
        with open(store_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.docstore = data["documents"]
        self.metadata = data["metadata"]
