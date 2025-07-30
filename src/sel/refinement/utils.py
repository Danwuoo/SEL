"""Utility classes for refinement tracing."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class RefineStep:
    """Data for a single refinement step."""

    version: int
    output: str
    feedback: str
    score: float


@dataclass
class RefinementTrace:
    """Container for multiple ``RefineStep`` entries."""

    steps: List[RefineStep] = field(default_factory=list)

