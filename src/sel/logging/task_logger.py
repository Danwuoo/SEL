"""Task logging interface."""

from __future__ import annotations

from typing import Dict, Optional

from .trace_schema import StepRecord, TaskTrace
from .writer import write_jsonl


class TaskLogger:
    """Simple task logger for recording episodes."""

    def __init__(self, log_path: str) -> None:
        self.log_path = log_path
        self.current: Optional[TaskTrace] = None

    def start_episode(self, task_id: str, meta: Dict) -> None:
        """Begin a new task episode."""
        self.current = TaskTrace(task_id=task_id, task_type=meta.get("type", ""), metadata=meta)

    def log_step(self, step_data: Dict) -> None:
        """Record a step in the current episode."""
        if self.current is None:
            raise RuntimeError("start_episode must be called first")
        record = StepRecord(
            step_id=step_data.get("step_id", len(self.current.steps)),
            prompt=step_data.get("prompt", ""),
            retrieved=step_data.get("retrieved", []),
            output=step_data.get("output", ""),
            reward=step_data.get("reward"),
        )
        self.current.steps.append(record)

    def log_refinement(self, version: int, feedback: str) -> None:
        """Add a refinement note to the latest step."""
        if self.current is None or not self.current.steps:
            raise RuntimeError("log_step must be called before log_refinement")
        self.current.steps[-1].refined_versions.append(f"{version}:{feedback}")

    def end_episode(self, result: Dict) -> None:
        """Finish the episode and store the result."""
        if self.current is None:
            raise RuntimeError("start_episode must be called first")
        self.current.result = result

    def save(self) -> None:
        """Persist the current trace to disk."""
        if self.current is None:
            raise RuntimeError("no episode to save")
        write_jsonl(self.current, self.log_path)
        self.current = None
