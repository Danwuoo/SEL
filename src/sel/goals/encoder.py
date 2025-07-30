from __future__ import annotations

from typing import Dict, List

import numpy as np

from sel.logging.trace_schema import TaskTrace


def encode_task_trajectory(tasks: List[TaskTrace]) -> np.ndarray:
    """Encode a sequence of task traces into a simple vector."""
    return np.array([len(t.steps) for t in tasks], dtype=float).reshape(len(tasks), 1)


def extract_behavioral_features(trace: TaskTrace) -> Dict:
    """Extract lightweight behavioral features from a trace."""
    return {"num_steps": len(trace.steps)}
