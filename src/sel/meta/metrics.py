"""Metric computations."""

from __future__ import annotations


def accuracy(pred: int, target: int) -> float:
    """Return a simple accuracy."""
    return float(pred == target)
