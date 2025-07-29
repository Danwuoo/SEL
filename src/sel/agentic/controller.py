"""Controller for running agentic episodes."""

from __future__ import annotations

from typing import Dict, List, Callable, TypedDict

from .agent import Agent
from .interface import TaskEnv


class TraceStep(TypedDict):
    """Single interaction step."""

    state: str
    action: str
    reward: float


class Trace(TypedDict):
    """Container for episode steps."""

    steps: List[TraceStep]


class AgenticController:
    """Simple agent-environment loop manager."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def run_episode(self, task: Dict, env: TaskEnv) -> Trace:
        """Run one episode and return a trace."""
        state = env.reset()
        done = False
        trace_steps: List[TraceStep] = []
        while not done:
            action = self.agent.act(str(state))
            state, reward, done, _info = env.step(action)
            trace_steps.append({"state": str(state), "action": action, "reward": reward})
        return {"steps": trace_steps}

    def run_batch(
        self, tasks: List[Dict], env_builder: Callable[[], TaskEnv]
    ) -> List[Trace]:
        """Run episodes for a batch of tasks."""
        traces: List[Trace] = []
        for task in tasks:
            traces.append(self.run_episode(task, env_builder()))
        return traces

