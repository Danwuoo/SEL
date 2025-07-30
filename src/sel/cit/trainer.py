"""Training utilities for Contrastive Instruction Tuning."""

from __future__ import annotations

import torch
from torch.utils.data import DataLoader

from .embedding_model import EmbeddingModel
from .loss import info_nce_loss

def train_cit_loop(
    model: EmbeddingModel,
    dataloader: DataLoader,
    optimizer: torch.optim.Optimizer,
    epochs: int = 1,
    device: str | torch.device = "cpu",
) -> None:
    """Run a basic CIT training loop."""

    model.model.to(device)
    model.model.train()
    for _ in range(epochs):
        for anchors, positives in dataloader:
            anchor_emb = model.encode(list(anchors)).to(device)
            positive_emb = model.encode(list(positives)).to(device)
            loss = info_nce_loss(anchor_emb, positive_emb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()


