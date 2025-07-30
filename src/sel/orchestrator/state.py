"""Training state tracking utilities."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class TrainingState:
    """Simple in-memory training state."""

    step: int = 0
    completed_tasks: List[str] = field(default_factory=list)
