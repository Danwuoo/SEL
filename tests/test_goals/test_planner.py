from sel.goals.planner import plan_goal


def test_plan_goal():
    assert plan_goal() == 'goal'
