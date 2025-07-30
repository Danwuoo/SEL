"""Data structures for critic results."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class CritiqueResult(BaseModel):
    """Structured output from a critic."""

    valid: bool
    score: Optional[float] = None
    error_types: List[str] = []
    summary: str
    suggestion: Optional[str] = None
