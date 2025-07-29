"""Environment interface and data models."""

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel


class TaskInput(BaseModel):
    """Input provided to the environment."""

    prompt: str


class TaskEnvironment:
    """Abstract environment providing tasks and feedback."""

    def present_task(self, task_input: TaskInput) -> Dict[str, Any]:
        """Return a context dictionary for the agent."""
        raise NotImplementedError

    def get_feedback(self, output: str) -> Dict[str, Any]:
        """Return feedback for a given agent output."""
        raise NotImplementedError


class EchoEnvironment(TaskEnvironment):
    """Simple environment that echoes inputs for testing."""

    def present_task(self, task_input: TaskInput) -> Dict[str, Any]:  # pragma: no cover - trivial
        return {"context": task_input.prompt}

    def get_feedback(self, output: str) -> Dict[str, Any]:  # pragma: no cover - trivial
        return {"feedback": output}


def communicate(message: str) -> str:
    """Backward compatible echo helper."""
    return message

