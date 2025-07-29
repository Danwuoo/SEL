"""Agent utilities for the agentic loop."""

from __future__ import annotations

from typing import Optional


class Agent:
    """Simple agent wrapper around a language model."""

    def act(self, prompt: str, context: Optional[str] = None) -> str:
        """Return an action for the given prompt."""
        if context:
            return f"{context}:{prompt}"
        return prompt

    def observe_and_refine(self, input_data: str) -> str:
        """Placeholder refinement step."""
        return input_data


def act() -> str:
    """Backward compatibility for old tests."""
    return "action"

