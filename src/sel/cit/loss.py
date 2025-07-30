"""Loss functions for CIT."""

from __future__ import annotations

import torch
try:  # pragma: no cover - optional dependency
    import torch.nn.functional as F
except Exception:  # pragma: no cover
    F = None


def compute_loss(pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """Return mean squared error.

    This simple loss is used by the unit tests. It is not meant for
    production training but provides a deterministic objective for basic
    verification.
    """

    return torch.mean((pred - target) ** 2)


def info_nce_loss(
    emb_a: torch.Tensor, emb_b: torch.Tensor, temperature: float = 0.07
) -> torch.Tensor:
    """Compute the InfoNCE loss for two embedding batches.

    Args:
        emb_a: Tensor of shape ``(batch, dim)`` representing anchor embeddings.
        emb_b: Tensor of shape ``(batch, dim)`` representing positive
            embeddings.
        temperature: Scaling factor for the logits.

    Returns:
        The contrastive loss encouraging matching pairs to have similar
        representations while treating other pairs in the batch as negatives.
    """

    if F is None:
        raise ImportError("PyTorch is required for info_nce_loss")

    emb_a = F.normalize(emb_a, dim=1)
    emb_b = F.normalize(emb_b, dim=1)
    logits = emb_a @ emb_b.T / temperature
    labels = torch.arange(emb_a.size(0), device=emb_a.device)
    return F.cross_entropy(logits, labels)
