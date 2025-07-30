from __future__ import annotations

from typing import List

from sel.logging.trace_schema import TaskTrace


class MemoryBank:
    """Lightweight store for past task traces."""

    def __init__(self) -> None:
        self._traces: List[TaskTrace] = []

    def push(self, trace: TaskTrace) -> None:
        """Add a trace to the memory bank."""
        self._traces.append(trace)

    def get_all(self) -> List[TaskTrace]:
        """Return all stored traces."""
        return list(self._traces)
