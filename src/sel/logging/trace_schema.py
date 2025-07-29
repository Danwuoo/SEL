"""Data structures for task logging."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class StepRecord:
    """Single step record."""

    step_id: int
    prompt: str
    retrieved: List[str]
    output: str
    reward: Optional[float] = None
    refined_versions: List[str] = field(default_factory=list)


@dataclass
class TaskTrace:
    """Container for a task episode."""

    task_id: str
    task_type: str
    metadata: Dict
    steps: List[StepRecord] = field(default_factory=list)
    result: Dict = field(default_factory=dict)
