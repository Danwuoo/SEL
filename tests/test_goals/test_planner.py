
from sel.goals import LatentGoalPlanner
from sel.goals.planner import plan_goal
from sel.logging.trace_schema import TaskTrace


def test_plan_goal() -> None:
    assert plan_goal() == "goal"


def test_latent_goal_planner() -> None:
    planner = LatentGoalPlanner()
    trace = TaskTrace(task_id="1", task_type="qa", metadata={"context": "math"})
    planner.update_goal_pool([trace])
    assert len(planner.goal_pool) == 1
    assert planner.goal_pool[0].context == "math"
