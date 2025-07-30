from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class MemoryEntry(BaseModel):
    """Single record stored in the :class:`MemoryBank`."""

    task_id: str
    task_type: str
    input_prompt: str
    output: str
    refined_output: Optional[str] = None
    embedding: Optional[List[float]] = None
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
