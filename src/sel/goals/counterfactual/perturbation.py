"""Utility functions for simple task perturbations."""

from __future__ import annotations


def simple_perturb(prompt: str) -> str:
    """A naive perturbation by requesting more detail."""
    return f"{prompt} Please explain in detail."
