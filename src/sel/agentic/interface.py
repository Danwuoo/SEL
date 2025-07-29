"""Environment interface definitions for the agentic loop."""

from __future__ import annotations

from typing import Any, Tuple


class TaskEnv:
    """Simple task environment protocol."""

    def reset(self) -> Any:
        """Reset the environment and return the initial state."""
        raise NotImplementedError

    def step(self, action: str) -> Tuple[Any, float, bool, dict]:
        """Advance one step given an action."""
        raise NotImplementedError


class EchoEnv(TaskEnv):
    """A minimal environment that echoes the agent's actions."""

    def __init__(self) -> None:
        self._done = False

    def reset(self) -> str:
        self._done = False
        return "start"

    def step(self, action: str) -> Tuple[str, float, bool, dict]:
        self._done = True
        return action, 1.0, self._done, {}

