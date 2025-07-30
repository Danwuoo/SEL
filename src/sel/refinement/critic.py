"""Simple critic implementation."""

from __future__ import annotations

from typing import Optional


def critique(output: str, prompt: str, context: Optional[str] = None) -> str:
    """Return a dummy critique for ``output`` given ``prompt`` and ``context``."""

    base = f"{prompt}" if context is None else f"{context}:{prompt}"
    if output != base:
        return "Looks good."  # Pretend the revision improved
    return "Needs more detail."
