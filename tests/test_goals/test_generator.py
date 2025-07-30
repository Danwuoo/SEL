from datetime import datetime

from sel.goals.generator import generate_subtasks
from sel.goals.goal_schema import LatentGoal


def test_generate_subtasks() -> None:
    goal = LatentGoal(
        goal_id="g1",
        name="Improve QA",
        type="strategy",
        context="qa",
        generated_from=["t1"],
        created_at=datetime.utcnow(),
    )
    subtasks = generate_subtasks(goal)
    assert subtasks[0]["goal_id"] == "g1"
