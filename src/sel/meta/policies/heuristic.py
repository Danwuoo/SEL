from __future__ import annotations

from typing import Dict, List

from ..curriculum_state import get_stats, update_stats


class HeuristicPolicy:
    """Rule-based curriculum selection policy."""

    def select(self, tasks: List[Dict], n: int) -> List[Dict]:
        """Return ``n`` tasks with lowest recent accuracy."""

        def _score(task: Dict) -> float:
            ttype = task.get("task_type", "generic")
            return get_stats(ttype).recent_accuracy

        ordered = sorted(tasks, key=_score)
        return ordered[:n]

    def update(self, task_type: str, result: Dict) -> None:
        """Update internal statistics based on ``result``."""

        update_stats(task_type, bool(result.get("success")), result.get("error_type"))
