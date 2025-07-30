"""Decision helpers for adapting training strategy."""

from __future__ import annotations

from typing import List

from .schema import TaskMetaStats


def decide_actions(stats: TaskMetaStats) -> List[str]:
    """Return a list of actions based on ``stats``."""
    actions: List[str] = []
    if stats.recent_success_rate < 0.5:
        actions.append("retrain")
    if stats.robustness_score < 0.7:
        actions.append("cit")
    return actions
