from sel.logging import TaskLogger


def test_task_logger_roundtrip(tmp_path):
    log_path = tmp_path / "log.jsonl"
    logger = TaskLogger(str(log_path))

    logger.start_episode("t1", {"type": "test"})
    logger.log_step({"step_id": 0, "prompt": "hi", "retrieved": [], "output": "hello", "reward": 1.0})
    logger.log_refinement(1, "ok")
    logger.end_episode({"status": "done"})
    logger.save()

    data = log_path.read_text().strip().split("\n")[0]
    assert "t1" in data
