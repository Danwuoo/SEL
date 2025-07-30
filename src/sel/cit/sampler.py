"""Dataset utilities for CIT."""

from __future__ import annotations

from typing import List, Tuple

from torch.utils.data import Dataset


class InstructionPairDataset(Dataset):
    """Simple dataset returning pairs of semantically equivalent instructions."""

    def __init__(self, pairs: List[Tuple[str, str]]) -> None:
        self.pairs = pairs

    def __len__(self) -> int:  # pragma: no cover - trivial
        return len(self.pairs)

    def __getitem__(self, idx: int) -> Tuple[str, str]:
        return self.pairs[idx]


def collate_batch(batch: List[Tuple[str, str]]) -> Tuple[List[str], List[str]]:
    """Return anchors and positives for a mini-batch."""

    anchors, positives = zip(*batch)
    return list(anchors), list(positives)
