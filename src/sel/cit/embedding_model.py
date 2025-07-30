"""Embedding model wrapper for CIT."""

from __future__ import annotations

from typing import List, Optional

import torch
from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """Thin wrapper around :class:`SentenceTransformer`."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2", device: Optional[str] = None) -> None:
        self.model = SentenceTransformer(model_name, device=device)

    def encode(self, text_batch: List[str]) -> torch.Tensor:
        """Encode ``text_batch`` and return ``torch.Tensor`` embeddings."""

        embeddings = self.model.encode(
            text_batch,
            convert_to_tensor=True,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return embeddings

