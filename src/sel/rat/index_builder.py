"""Utilities to build retrieval indices."""

from __future__ import annotations

from typing import List, Optional

from .retriever import SemanticRetriever


def build_index(docs: List[str], metadata: Optional[List[dict]] = None, output_path: str = "rat_index") -> SemanticRetriever:
    """Build a new index from ``docs`` and save it to ``output_path``."""

    retriever = SemanticRetriever()
    retriever.index_documents(docs, metadata)
    retriever.save_index(output_path)
    return retriever
