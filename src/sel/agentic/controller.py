"""Agentic loop controller implementation."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

from pydantic import BaseModel

from .agent import BaseAgent
from .interface import TaskEnvironment, TaskInput


class InteractionRound(BaseModel):
    """Single interaction step."""

    context: str
    decision: str
    feedback: Dict[str, object]


class InteractionTrace(BaseModel):
    """Trace of an episode."""

    rounds: List[InteractionRound] = []
    started_at: datetime


class AgenticLoopController:
    """Orchestrates agent-environment interactions."""

    def __init__(self, agent: BaseAgent, env: TaskEnvironment) -> None:
        self.agent = agent
        self.env = env
        self.trace: List[InteractionRound] = []

    def reset_state(self) -> None:
        """Reset the internal trace state."""
        self.trace = []

    def integrate_feedback(self, feedback: Dict[str, object]) -> None:  # pragma: no cover - stub
        """Hook to integrate feedback (placeholder)."""
        _ = feedback

    def run_episode(
        self,
        task_input: TaskInput,
        n_rounds: int = 1,
        save_path: Optional[str] = None,
    ) -> InteractionTrace:
        """Execute a task episode."""

        self.reset_state()
        context_dict = self.env.present_task(task_input)
        context = context_dict.get("context", task_input.prompt)
        for _ in range(n_rounds):
            decision = self.agent.decide(context)
            feedback = self.env.get_feedback(decision)
            self.integrate_feedback(feedback)
            self.trace.append(
                InteractionRound(context=context, decision=decision, feedback=feedback)
            )
            context = feedback.get("next_context", context)
        trace = InteractionTrace(rounds=self.trace, started_at=datetime.utcnow())

        if save_path:
            path = Path(save_path)
            with path.open("w", encoding="utf-8") as f:
                for r in trace.rounds:
                    f.write(r.json() + "\n")

        return trace


def run() -> None:  # pragma: no cover - CLI helper
    """Run the agentic loop with dummy components."""
    from .agent import DummyAgent
    from .interface import EchoEnvironment, TaskInput

    controller = AgenticLoopController(DummyAgent(), EchoEnvironment())
    trace = controller.run_episode(TaskInput(prompt="hello"))
    print(trace.json())

