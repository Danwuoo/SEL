"""Utilities for the Retrieval-Augmented Training module."""

from __future__ import annotations

from typing import Iterable, List

import numpy as np
from sentence_transformers import SentenceTransformer


def normalize(text: str) -> str:
    """Return a lowercased version of ``text``."""

    return text.lower()


def chunk_text(text: str, max_length: int = 512) -> List[str]:
    """Split ``text`` into newline-delimited chunks not exceeding ``max_length``."""

    lines = text.splitlines()
    chunks: List[str] = []
    current = ""
    for line in lines:
        if len(current) + len(line) + 1 > max_length:
            if current:
                chunks.append(current.strip())
                current = ""
        current += line + "\n"
    if current:
        chunks.append(current.strip())
    return chunks


def embed_batch(model: SentenceTransformer, texts: Iterable[str]) -> np.ndarray:
    """Encode ``texts`` using ``model`` and return ``float32`` embeddings."""

    embeddings = model.encode(
        list(texts),
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )
    return embeddings.astype("float32")
