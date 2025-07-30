"""Base critic class definition."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from .schema import CritiqueResult


class BaseCritic(ABC):
    """Abstract base class for critics."""

    @abstractmethod
    def critique(self, prompt: str, output: str, context: Optional[str] = None) -> CritiqueResult:
        """Return a :class:`CritiqueResult` for ``output`` given ``prompt`` and ``context``."""
        raise NotImplementedError
