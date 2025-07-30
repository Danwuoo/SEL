from __future__ import annotations

import random
from typing import List

from .schema import MemoryEntry


def sample_diversity(entries: List[MemoryEntry], n: int) -> List[MemoryEntry]:
    """Return ``n`` random entries."""

    if not entries:
        return []
    return random.sample(entries, min(n, len(entries)))
