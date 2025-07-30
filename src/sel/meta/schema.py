"""Data schemas for meta-cognitive loop."""

from __future__ import annotations

from typing import Dict

from pydantic import BaseModel


class TaskMetaStats(BaseModel):
    """Summary statistics for a single task type."""

    task_id: str
    type: str
    recent_success_rate: float = 0.0
    error_freq: Dict[str, int] = {}
    refinement_improvement: float = 0.0
    robustness_score: float = 0.0

