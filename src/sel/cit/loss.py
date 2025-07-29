"""Loss function placeholders."""

from __future__ import annotations

try:
    import torch  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    from typing import Any

    class _Tensor(list):
        def __sub__(self, other: Any) -> "_Tensor":
            return _Tensor([a - b for a, b in zip(self, other)])

        def __pow__(self, exp: int) -> "_Tensor":
            return _Tensor([float(x) ** exp for x in self])

        def __truediv__(self, other: Any) -> "_Tensor":
            return _Tensor([x / other for x in self])

        def mean(self) -> "_Tensor":  # type: ignore[override]
            return _Tensor([sum(self) / len(self)])

        def item(self) -> float:
            return self[0] if self else 0.0

    def tensor(data: Any) -> _Tensor:  # pragma: no cover - fallback
        return _Tensor(list(data))

    torch = type("torch", (), {"Tensor": _Tensor, "tensor": tensor, "mean": lambda x: x.mean()})()  # type: ignore


def compute_loss(pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """Return mean squared error."""
    diff = pred - target
    squared = diff ** 2
    if hasattr(torch, "mean"):
        return torch.mean(squared)
    return squared.mean()
