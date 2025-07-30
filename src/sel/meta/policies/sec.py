from __future__ import annotations

from typing import Dict, List

from ..curriculum_state import update_stats

from .bandit import UCB1


class SECPPolicy:
    """Self-Evolving Curriculum policy based on learning gain."""

    def __init__(self) -> None:
        self.bandit = UCB1()

    def select(self, tasks: List[Dict], n: int) -> List[Dict]:
        picked: List[Dict] = []
        remaining = list(tasks)
        for _ in range(n):
            if not remaining:
                break
            arms = list({t["task_type"] for t in remaining})
            arm = self.bandit.select(arms)
            for i, t in enumerate(remaining):
                if t["task_type"] == arm:
                    picked.append(t)
                    remaining.pop(i)
                    break
        return picked

    def update(self, task_type: str, result: Dict) -> None:
        stats = update_stats(task_type, bool(result.get("success")), result.get("error_type"))
        self.bandit.update(task_type, stats.learning_gain)
