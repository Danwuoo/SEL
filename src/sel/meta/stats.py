"""Utilities for analyzing training statistics."""

from __future__ import annotations

from statistics import mean, stdev
from typing import Iterable


def moving_average(values: Iterable[float]) -> float:
    """Return the average of ``values`` or ``0.0`` if empty."""
    vals = list(values)
    return mean(vals) if vals else 0.0


def task_volatility(scores: Iterable[float]) -> float:
    """Return the standard deviation of ``scores`` or ``0.0`` if insufficient."""
    vals = list(scores)
    return stdev(vals) if len(vals) > 1 else 0.0
