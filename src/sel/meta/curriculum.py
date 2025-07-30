"""Curriculum management utilities."""

from __future__ import annotations

from typing import Dict, List, Sequence

from .policies import HeuristicPolicy


class CurriculumManager:
    """Manage task sampling and feedback using a selection policy."""

    def __init__(self, policy: HeuristicPolicy | None = None) -> None:
        self.policy = policy or HeuristicPolicy()
        self._queue: List[Dict] = []

    def add_tasks(self, tasks: Sequence[Dict]) -> None:
        self._queue.extend(tasks)

    def select_tasks(self, n: int) -> List[Dict]:
        if not self._queue:
            return []
        picked = self.policy.select(self._queue, n)
        for task in picked:
            self._queue.remove(task)
        return picked

    def update_feedback(self, task_id: str, result: Dict) -> None:
        task_type = result.get("task_type", "generic")
        self.policy.update(task_type, result)


_DEFAULT_MANAGER = CurriculumManager()


def add_tasks(tasks: Sequence[Dict]) -> None:
    """Add tasks to the curriculum."""

    _DEFAULT_MANAGER.add_tasks(tasks)


def select_next_tasks(n: int = 10) -> List[Dict]:
    """Return up to ``n`` tasks from the queue."""

    return _DEFAULT_MANAGER.select_tasks(n)


def update_curriculum(task_feedback: Dict) -> None:
    """Update the curriculum based on ``task_feedback``."""

    task_id = task_feedback.get("task_id", "")
    _DEFAULT_MANAGER.update_feedback(task_id, task_feedback)
    new_tasks = task_feedback.get("new_tasks")
    if new_tasks:
        add_tasks(new_tasks)
