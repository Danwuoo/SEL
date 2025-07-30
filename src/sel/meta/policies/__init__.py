"""Curriculum selection policies."""

from .heuristic import HeuristicPolicy
from .bandit import UCBBanditPolicy
from .sec import SECPPolicy

__all__ = ["HeuristicPolicy", "UCBBanditPolicy", "SECPPolicy"]
