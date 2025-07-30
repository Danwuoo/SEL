"""Task scheduling utilities for the training orchestrator."""

from __future__ import annotations

from typing import Dict, List


class Scheduler:
    """Simple FIFO scheduler."""

    def __init__(self, tasks: List[Dict] | None = None) -> None:
        self.tasks: List[Dict] = list(tasks or [])

    def add_tasks(self, tasks: List[Dict]) -> None:
        self.tasks.extend(tasks)

    def get_task_batch(self, batch_size: int = 1, phase: str = "main") -> List[Dict]:
        batch = self.tasks[:batch_size]
        self.tasks = self.tasks[batch_size:]
        return batch

    def get_active_modules(self, task: Dict) -> List[str]:
        return ["rat", "refinement"]
