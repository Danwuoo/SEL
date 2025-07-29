"""Utilities for simple policy manipulations."""

from __future__ import annotations

from typing import Sequence

import numpy as np


def softmax(logits: Sequence[float], temperature: float = 1.0) -> np.ndarray:
    """Compute a temperature-scaled softmax."""
    scaled = np.array(logits, dtype=float) / max(temperature, 1e-5)
    e = np.exp(scaled - np.max(scaled))
    return e / np.sum(e)


def top_k_mask(logits: Sequence[float], k: int) -> np.ndarray:
    """Return logits masked to the top-k values."""
    arr = np.array(logits, dtype=float)
    if k <= 0:
        return arr
    indices = np.argsort(arr)[-k:]
    mask = np.full_like(arr, -np.inf)
    mask[indices] = arr[indices]
    return mask
