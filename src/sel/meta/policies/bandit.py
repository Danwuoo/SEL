from __future__ import annotations

import math
from typing import Dict, List

from ..curriculum_state import update_stats


class UCB1:
    """Simple UCB1 multi-armed bandit implementation."""

    def __init__(self) -> None:
        self.counts: Dict[str, int] = {}
        self.values: Dict[str, float] = {}

    def select(self, arms: List[str]) -> str:
        for arm in arms:
            if self.counts.get(arm, 0) == 0:
                return arm

        total = sum(self.counts[a] for a in arms)
        scores = {
            a: self.values.get(a, 0.0)
            + math.sqrt(2 * math.log(total) / self.counts[a])
            for a in arms
        }
        return max(scores, key=scores.get)

    def update(self, arm: str, reward: float) -> None:
        n = self.counts.get(arm, 0) + 1
        self.counts[arm] = n
        value = self.values.get(arm, 0.0)
        self.values[arm] = ((n - 1) / n) * value + (1 / n) * reward


class UCBBanditPolicy:
    """Curriculum policy based on UCB1 bandit."""

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
        success = bool(result.get("success"))
        update_stats(task_type, success, result.get("error_type"))
        self.bandit.update(task_type, 1.0 if success else 0.0)
