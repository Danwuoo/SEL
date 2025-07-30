"""Evaluation helpers for CIT."""

from __future__ import annotations

from typing import List, Tuple

import torch

from .embedding_model import EmbeddingModel


def evaluate_similarity(model: EmbeddingModel, pairs: List[Tuple[str, str]]) -> float:
    """Return average cosine similarity for instruction pairs."""

    with torch.no_grad():
        emb_a = model.encode([p[0] for p in pairs])
        emb_b = model.encode([p[1] for p in pairs])
        sims = torch.nn.functional.cosine_similarity(emb_a, emb_b)
    return sims.mean().item()

