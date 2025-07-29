from sel.logging.replay_loader import load_episode
from sel.logging.task_logger import TaskLogger


def test_load_episode(tmp_path):
    log_path = tmp_path / "log.jsonl"
    logger = TaskLogger(str(log_path))

    logger.start_episode("task_x", {"type": "test"})
    logger.log_step({"step_id": 0, "prompt": "p", "retrieved": [], "output": "o"})
    logger.end_episode({"status": "done"})
    logger.save()

    trace = load_episode("task_x", str(log_path))
    assert trace is not None
    assert trace.task_id == "task_x"
