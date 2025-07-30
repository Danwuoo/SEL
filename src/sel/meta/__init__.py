"""Meta-cognitive loop utilities."""

from .adaptation import decide_actions
from .curriculum import (
    CurriculumManager,
    add_tasks,
    select_next_tasks,
    update_curriculum,
)
from .curriculum_state import TaskTypeStats, get_stats, reset_stats, update_stats
from .monitor import aggregate_stats, record_task_result
from .policies import HeuristicPolicy, SECPPolicy, UCBBanditPolicy
from .schema import TaskMetaStats
from .selector import pick_for_refinement
from .stats import moving_average, task_volatility

__all__ = [
    "decide_actions",
    "add_tasks",
    "select_next_tasks",
    "update_curriculum",
    "CurriculumManager",
    "HeuristicPolicy",
    "UCBBanditPolicy",
    "SECPPolicy",
    "TaskTypeStats",
    "get_stats",
    "update_stats",
    "reset_stats",
    "aggregate_stats",
    "record_task_result",
    "TaskMetaStats",
    "pick_for_refinement",
    "moving_average",
    "task_volatility",
]
