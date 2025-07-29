"""Utilities for loading and querying logged episodes."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, List, Optional

from .trace_schema import StepRecord, TaskTrace


def _dict_to_trace(data: dict) -> TaskTrace:
    steps = [
        StepRecord(
            step_id=s["step_id"],
            prompt=s["prompt"],
            retrieved=s.get("retrieved", []),
            output=s.get("output", ""),
            reward=s.get("reward"),
            refined_versions=s.get("refined_versions", []),
        )
        for s in data.get("steps", [])
    ]
    return TaskTrace(
        task_id=data["task_id"],
        task_type=data.get("task_type", ""),
        metadata=data.get("metadata", {}),
        steps=steps,
        result=data.get("result", {}),
    )


def load_episode(task_id: str, log_path: str) -> Optional[TaskTrace]:
    """Load a specific episode trace from a JSONL log file."""
    file = Path(log_path)
    if not file.exists():
        return None
    with file.open("r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if data.get("task_id") == task_id:
                return _dict_to_trace(data)
    return None


def list_failed_tasks(log_path: str, filter_fn: Callable[[dict], bool]) -> List[str]:
    """Return task IDs that match ``filter_fn`` from the log file."""
    file = Path(log_path)
    tasks: List[str] = []
    if not file.exists():
        return tasks
    with file.open("r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if filter_fn(data):
                tasks.append(data["task_id"])
    return tasks
