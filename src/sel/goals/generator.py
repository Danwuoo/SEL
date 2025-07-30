"""Generate concrete tasks from latent goals."""

from __future__ import annotations

from typing import Dict, List

from .goal_schema import LatentGoal


def generate(seed: int) -> str:
    """Generate a goal string based on a seed."""
    return f"goal-{seed}"


def generate_subtasks(goal: LatentGoal) -> List[Dict]:
    """Produce simple subtasks that aim to achieve the provided goal."""
    prompt = f"Achieve: {goal.name}"
    return [{"goal_id": goal.goal_id, "prompt": prompt}]
