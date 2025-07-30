"""Generate counterfactual tasks from past traces."""

from __future__ import annotations

from uuid import uuid4

from sel.logging.trace_schema import TaskTrace

from .perturbation import simple_perturb
from .schema import GeneratedTask
from .templates import TEMPLATES


def generate(task_trace: TaskTrace, mode: str = "robustness") -> GeneratedTask:
    """Create a counterfactual task variant for the given trace."""
    base_prompt = task_trace.steps[0].prompt if task_trace.steps else ""
    modified = simple_perturb(base_prompt)
    template = TEMPLATES.get(mode, "{prompt}")
    final_prompt = template.format(prompt=modified)
    return GeneratedTask(
        origin_task_id=task_trace.task_id,
        counterfactual_id=str(uuid4()),
        mode=mode,
        modified_prompt=final_prompt,
        modification_reason="simple perturbation",
        original_context=task_trace.metadata.get("context"),
    )
