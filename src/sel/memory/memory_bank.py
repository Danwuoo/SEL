from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import Dict, List

from .schema import MemoryEntry


class MemoryBank:
    """Simple in-memory storage bucket for :class:`MemoryEntry` objects."""

    def __init__(self) -> None:
        self._store: Dict[str, List[MemoryEntry]] = defaultdict(list)

    def add_entry(self, entry: MemoryEntry) -> None:
        """Add ``entry`` to the bank grouped by its ``task_type``."""

        self._store[entry.task_type].append(entry)

    def get_entries(self, task_type: str | None = None) -> List[MemoryEntry]:
        """Return all entries or those under ``task_type``."""

        if task_type is None:
            entries: List[MemoryEntry] = []
            for bucket in self._store.values():
                entries.extend(bucket)
            return entries
        return list(self._store.get(task_type, []))

    def remove_before(self, ts: datetime) -> None:
        """Delete entries created prior to ``ts``."""

        for key in list(self._store.keys()):
            self._store[key] = [e for e in self._store[key] if e.created_at >= ts]
            if not self._store[key]:
                del self._store[key]
