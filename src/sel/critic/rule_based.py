"""Simple rule-based critic helpers."""

from __future__ import annotations

from typing import Optional

from .base_critic import BaseCritic
from .schema import CritiqueResult


class RuleBasedCritic(BaseCritic):
    """Critic that applies basic rules for code snippets."""

    def critique(self, prompt: str, output: str, context: Optional[str] = None) -> CritiqueResult:
        errors = []
        if "TODO" in output or "pass" in output:
            errors.append("incomplete")
        valid = not errors
        summary = "Looks good." if valid else "Output seems incomplete."
        return CritiqueResult(valid=valid, score=None, error_types=errors, summary=summary)
