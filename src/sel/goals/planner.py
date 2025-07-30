"""Goal planner utilities for latent goal formation."""

from __future__ import annotations

from datetime import datetime
from typing import List

from sel.logging.trace_schema import TaskTrace

from .goal_schema import LatentGoal


def plan_goal() -> str:
    """Return a dummy goal."""
    return "goal"


class LatentGoalPlanner:
    """Simple planner that derives goals from task traces."""

    def __init__(self) -> None:
        self.goal_pool: List[LatentGoal] = []

    def identify_latent_goals(self, task_traces: List[TaskTrace]) -> List[LatentGoal]:
        """Create latent goals from task contexts."""
        goals: List[LatentGoal] = []
        for trace in task_traces:
            context = trace.metadata.get("context", "default")
            goals.append(
                LatentGoal(
                    goal_id=f"{trace.task_id}-goal",
                    name=f"Improve {context}",
                    type="strategy",
                    context=context,
                    generated_from=[trace.task_id],
                    created_at=datetime.utcnow(),
                    priority=1.0,
                )
            )
        return goals

    def update_goal_pool(self, task_traces: List[TaskTrace]) -> None:
        """Update the internal goal pool with new latent goals."""
        self.goal_pool.extend(self.identify_latent_goals(task_traces))
