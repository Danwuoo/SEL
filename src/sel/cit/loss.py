"""Loss function placeholders."""

from __future__ import annotations

import torch


def compute_loss(pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """Return mean squared error."""
    return torch.mean((pred - target) ** 2)
