"""Scorer functions for comparing text versions."""

from __future__ import annotations

from difflib import SequenceMatcher


def score(original: str, new: str) -> float:
    """Return a similarity score between ``original`` and ``new``."""

    return SequenceMatcher(None, original, new).ratio()
