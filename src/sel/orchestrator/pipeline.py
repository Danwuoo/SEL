"""Core training orchestrator pipeline."""

from __future__ import annotations

from typing import Optional

from .config import PipelineConfig
from .hooks import run_cit_finetune, run_rat, run_refinement
from .scheduler import Scheduler
from .state import TrainingState


def run_pipeline(config: Optional[PipelineConfig] = None) -> None:
    """Run the orchestrator pipeline."""
    print("pipeline running")
    sched = Scheduler()
    sched.add_tasks([{"task_id": "t1"}])
    state = TrainingState()
    batch_size = config.batch_size if config else 1
    tasks = sched.get_task_batch(batch_size)
    for task in tasks:
        output = run_rat(task)
        output = run_refinement(output)
        state.completed_tasks.append(task["task_id"])
        state.step += 1
    run_cit_finetune(tasks)
    print(f"completed {state.step} steps")
