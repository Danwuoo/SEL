"""Agent definitions for the agentic loop."""

from __future__ import annotations




class BaseAgent:
    """Minimal interface for an agent used in the loop."""

    def decide(self, context: str) -> str:
        """Return an action for the given context."""
        raise NotImplementedError

    def refine(self, draft: str) -> str:  # pragma: no cover - optional
        """Optional refinement step. Returns the refined output."""
        return draft


class DummyAgent(BaseAgent):
    """Simple agent used for tests and examples."""

    def decide(self, context: str) -> str:  # pragma: no cover - trivial
        return "action"


def act() -> str:
    """Backward compatible function for existing tests."""
    return DummyAgent().decide("")

