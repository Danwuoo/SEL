"""Curriculum management utilities."""

from __future__ import annotations

from typing import Dict, List, Sequence

_TASK_QUEUE: List[Dict] = []


def add_tasks(tasks: Sequence[Dict]) -> None:
    """Add tasks to the curriculum."""
    _TASK_QUEUE.extend(tasks)


def select_next_tasks(n: int = 10) -> List[Dict]:
    """Return up to ``n`` tasks from the queue."""
    return list(_TASK_QUEUE[:n])


def update_curriculum(task_feedback: Dict) -> None:
    """Naively update the curriculum based on ``task_feedback``."""
    new_tasks = task_feedback.get("new_tasks")
    if new_tasks:
        add_tasks(new_tasks)
