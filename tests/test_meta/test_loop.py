from sel.meta import (
    TaskMetaStats,
    add_tasks,
    aggregate_stats,
    decide_actions,
    pick_for_refinement,
    record_task_result,
    select_next_tasks,
)


def test_monitor_aggregate():
    record_task_result("t1", {"success": True})
    record_task_result("t1", {"success": False, "error_type": "x"})
    stats = aggregate_stats(2)
    assert 0.5 <= stats.recent_success_rate <= 1.0
    assert stats.error_freq["x"] == 1


def test_curriculum_select():
    add_tasks([{"id": 1}, {"id": 2}])
    tasks = select_next_tasks(1)
    assert tasks[0]["id"] == 1


def test_adaptation_actions():
    stats = TaskMetaStats(task_id="t", type="", recent_success_rate=0.4, robustness_score=0.6)
    actions = decide_actions(stats)
    assert "retrain" in actions and "cit" in actions


def test_selector_pick():
    r1 = TaskMetaStats(task_id="a", type="", recent_success_rate=0.7)
    r2 = TaskMetaStats(task_id="b", type="", recent_success_rate=0.9)
    picked = pick_for_refinement([r1, r2], threshold=0.8)
    assert picked == ["a"]
