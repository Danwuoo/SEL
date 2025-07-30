from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class GeneratedTask:
    """Representation of a counterfactual task variant."""

    origin_task_id: str
    counterfactual_id: str
    mode: str
    modified_prompt: str
    modification_reason: str
    original_context: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
