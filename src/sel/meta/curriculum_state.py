from __future__ import annotations

from collections import Counter
from typing import Dict, Optional

from pydantic import BaseModel, Field


class TaskTypeStats(BaseModel):
    """Track statistics for a particular task type."""

    task_type: str
    recent_accuracy: float = 0.0
    learning_gain: float = 0.0
    failure_mode: Counter[str] = Field(default_factory=Counter)
    num_attempts: int = 0


_STATS: Dict[str, TaskTypeStats] = {}


def reset_stats() -> None:
    """Clear all tracked statistics."""

    _STATS.clear()


def get_stats(task_type: str) -> TaskTypeStats:
    """Return stats for ``task_type`` or a default one."""

    return _STATS.get(task_type, TaskTypeStats(task_type=task_type))


def update_stats(task_type: str, success: bool, error: Optional[str] = None) -> TaskTypeStats:
    """Update statistics for ``task_type`` and return the record."""

    stats = _STATS.get(task_type)
    if stats is None:
        stats = TaskTypeStats(task_type=task_type)
        _STATS[task_type] = stats

    prev_accuracy = stats.recent_accuracy
    stats.num_attempts += 1
    stats.recent_accuracy = (
        (stats.recent_accuracy * (stats.num_attempts - 1) + (1 if success else 0))
        / stats.num_attempts
    )
    stats.learning_gain = stats.recent_accuracy - prev_accuracy

    if not success and error:
        stats.failure_mode[error] = stats.failure_mode.get(error, 0) + 1

    return stats
