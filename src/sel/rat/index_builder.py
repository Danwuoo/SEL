"""Utilities to build retrieval indices."""

from __future__ import annotations

from typing import List, Optional

from .retriever import SemanticRetriever


def build_index(
    docs: List[str],
    metadata: Optional[List[dict]] = None,
    output_path: str = "rat_index",
    retriever: Optional[SemanticRetriever] = None,
    encoder_model: str = "sentence-transformers/all-MiniLM-L6-v2",
) -> SemanticRetriever:
    """
    Build a new index from ``docs`` and save it to ``output_path``.

    Args:
        docs: A list of documents to index.
        metadata: Optional metadata for each document.
        output_path: The path to save the index to.
        retriever: An existing retriever instance to use. If None, a new one is created.
        encoder_model: The name of the sentence-transformer model to use.

    Returns:
        The retriever with the indexed documents.
    """
    if retriever is None:
        retriever = SemanticRetriever(encoder_model=encoder_model)

    retriever.index_documents(docs, metadata)
    retriever.save_index(output_path)
    return retriever
