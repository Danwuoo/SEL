"""Memory management utilities."""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Union

from sel.logging.trace_schema import TaskTrace

from .filter import sample_diversity
from .memory_bank import MemoryBank
from .retriever import query_memory
from .schema import MemoryEntry


class MemoryManager:
    """High level API for storing and retrieving task traces."""

    def __init__(self) -> None:
        self.bank = MemoryBank()

    def store_trace(self, task_id: str, trace: TaskTrace) -> MemoryEntry:
        """Convert ``trace`` to :class:`MemoryEntry` and store it."""

        prompt = trace.steps[0].prompt if trace.steps else ""
        output = trace.steps[-1].output if trace.steps else ""
        entry = MemoryEntry(
            task_id=task_id,
            task_type=trace.task_type,
            input_prompt=prompt,
            output=output,
        )
        self.bank.add_entry(entry)
        return entry

    def retrieve(
        self, query: Union[str, Dict[str, str]], top_k: int = 5
    ) -> List[MemoryEntry]:
        """Return entries matching ``query``."""

        if isinstance(query, dict):
            task_type = query.get("task_type")
            entries = self.bank.get_entries(task_type)
            return entries[:top_k]
        return query_memory(query, self.bank, top_k=top_k)

    def sample_for_replay(self, strategy: str = "diversity", n: int = 10) -> List[MemoryEntry]:
        """Return ``n`` entries for replay."""

        entries = self.bank.get_entries()
        if strategy == "diversity":
            return sample_diversity(entries, n)
        return entries[:n]

    def prune_old_data(self, before: datetime) -> None:
        """Remove entries older than ``before``."""

        self.bank.remove_before(before)
