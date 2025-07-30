"""LLM-based critic implementation (mock)."""

from __future__ import annotations

from typing import Optional

from .base_critic import BaseCritic
from .schema import CritiqueResult


class LlmCritic(BaseCritic):
    """Trivial LLM critic used for tests."""

    def critique(self, prompt: str, output: str, context: Optional[str] = None) -> CritiqueResult:
        base = f"{prompt}" if context is None else f"{context}:{prompt}"
        valid = output != base
        summary = "Looks good." if valid else "Needs more detail."
        score = 1.0 if valid else 0.0
        return CritiqueResult(valid=valid, score=score, error_types=[], summary=summary)
