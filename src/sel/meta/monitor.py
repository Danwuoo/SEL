"""Monitor training results and compute statistics."""

from __future__ import annotations

from collections import deque
from typing import Deque, Dict, List

from .schema import TaskMetaStats

# In-memory history of task metrics
_HISTORY: Deque[Dict] = deque()


def record_task_result(task_id: str, metrics: Dict) -> None:
    """Record the outcome of a task."""
    entry = {"task_id": task_id, **metrics}
    _HISTORY.append(entry)


def aggregate_stats(window_size: int = 100) -> TaskMetaStats:
    """Aggregate recent stats into a :class:`TaskMetaStats`."""
    recent: List[Dict] = list(_HISTORY)[-window_size:]
    if not recent:
        return TaskMetaStats(task_id="*", type="aggregate")

    success_count = sum(1 for r in recent if r.get("success"))
    error_freq: Dict[str, int] = {}
    for r in recent:
        err = r.get("error_type")
        if err:
            error_freq[err] = error_freq.get(err, 0) + 1

    return TaskMetaStats(
        task_id="*",
        type="aggregate",
        recent_success_rate=success_count / len(recent),
        error_freq=error_freq,
    )
