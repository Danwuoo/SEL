"""Sample selection helpers."""

from __future__ import annotations

from typing import List

from .schema import TaskMetaStats


def pick_for_refinement(records: List[TaskMetaStats], threshold: float = 0.8) -> List[str]:
    """Return task IDs with success rate below ``threshold``."""
    return [r.task_id for r in records if r.recent_success_rate < threshold]
