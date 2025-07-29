"""Cache utilities."""

from __future__ import annotations

_cache = {}


def get(key: str) -> str | None:
    """Retrieve from cache."""
    return _cache.get(key)


def set(key: str, value: str) -> None:
    """Set cache value."""
    _cache[key] = value
