"""Self-refinement loop implementation."""

from __future__ import annotations

from typing import Dict, Optional

from .critic import critique
from .scorer import score
from .utils import RefineStep, RefinementTrace


def run_refinement(
    prompt: str, context: Optional[str] = None, max_rounds: int = 1
) -> Dict[str, object]:
    """Run a simple self-refinement loop.

    Parameters
    ----------
    prompt:
        Initial prompt or draft to refine.
    context:
        Optional context to prepend when generating a new version.
    max_rounds:
        Maximum number of refinement iterations.

    Returns
    -------
    Dict[str, object]
        Dictionary containing the final ``refined_output`` and a
        ``RefinementTrace`` under ``trace``.
    """

    output = prompt
    trace = RefinementTrace()
    for i in range(max_rounds):
        feedback = critique(output, prompt, context)
        new_output = f"{context + ':' if context else ''}{output} {feedback}"
        improvement = score(output, new_output)
        trace.steps.append(
            RefineStep(
                version=i,
                output=new_output,
                feedback=feedback,
                score=improvement,
            )
        )
        output = new_output

    return {"refined_output": output, "trace": trace}

