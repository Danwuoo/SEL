from __future__ import annotations

from typing import Callable, Iterable, List

import numpy as np

from .memory_bank import MemoryBank
from .schema import MemoryEntry


def _semantic_search(
    query_vec: Iterable[float], entries: List[MemoryEntry], top_k: int
) -> List[MemoryEntry]:
    """Return ``top_k`` entries ranked by dot product similarity."""

    q = np.array(list(query_vec))
    results = []
    for e in entries:
        if e.embedding is None:
            continue
        sim = float(np.dot(q, np.array(e.embedding)))
        results.append((sim, e))
    results.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in results[:top_k]]


def query_memory(
    query: str | Iterable[float],
    memory_bank: MemoryBank,
    mode: str = "keyword",
    embedding_model: object | None = None,
    top_k: int = 5,
    filter_fn: Callable[[MemoryEntry], bool] | None = None,
) -> List[MemoryEntry]:
    """Retrieve entries from ``memory_bank`` matching ``query``."""

    entries = memory_bank.get_entries()
    if filter_fn is not None:
        entries = [e for e in entries if filter_fn(e)]

    if mode == "semantic":
        if isinstance(query, str):
            if embedding_model is None:
                raise ValueError("embedding_model required for semantic search")
            vec = embedding_model.encode([query])[0]
        else:
            vec = query
        return _semantic_search(vec, entries, top_k)

    # keyword search
    result = [
        e
        for e in entries
        if isinstance(query, str)
        and (query in e.input_prompt or query in e.output)
    ]
    return result[:top_k]
