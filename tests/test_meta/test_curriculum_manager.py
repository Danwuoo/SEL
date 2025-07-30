from sel.meta import (
    CurriculumManager,
    HeuristicPolicy,
    get_stats,
    reset_stats,
    update_stats,
)


def setup_function(_) -> None:
    reset_stats()


def test_update_stats() -> None:
    update_stats("qa", True)
    update_stats("qa", False, "x")
    stats = get_stats("qa")
    assert stats.num_attempts == 2
    assert stats.failure_mode["x"] == 1


def test_heuristic_select() -> None:
    policy = HeuristicPolicy()
    tasks = [
        {"task_id": "t1", "task_type": "a"},
        {"task_id": "t2", "task_type": "b"},
    ]
    update_stats("a", False)
    update_stats("b", True)
    picked = policy.select(tasks, 1)
    assert picked[0]["task_type"] == "a"


def test_curriculum_manager_cycle() -> None:
    manager = CurriculumManager(policy=HeuristicPolicy())
    manager.add_tasks([{"task_id": "t1", "task_type": "a"}])
    tasks = manager.select_tasks(1)
    assert tasks[0]["task_id"] == "t1"
    manager.update_feedback("t1", {"success": True, "task_type": "a"})
    stats = get_stats("a")
    assert stats.recent_accuracy == 1.0
