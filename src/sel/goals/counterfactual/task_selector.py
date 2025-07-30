"""Select traces suitable for counterfactual generation."""

from __future__ import annotations

from typing import List

from sel.logging.trace_schema import TaskTrace


def select_for_counterfactual(buffer: List[TaskTrace], mode: str) -> List[TaskTrace]:
    """Return traces that failed and are candidates for counterfactuals."""
    candidates: List[TaskTrace] = []
    for trace in buffer:
        if not trace.result.get("success", False):
            candidates.append(trace)
    return candidates
