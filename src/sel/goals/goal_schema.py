from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class LatentGoal:
    """Representation of a latent capability goal."""

    goal_id: str
    name: str
    type: str
    context: str
    generated_from: List[str]
    priority: float = 1.0
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class GeneratedTask:
    """Simple structure for a generated subtask."""

    goal_id: str
    prompt: str
