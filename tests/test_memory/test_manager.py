from datetime import datetime, timedelta

from sel.memory import MemoryManager
from sel.logging.trace_schema import StepRecord, TaskTrace


def _make_trace(task_id: str) -> TaskTrace:
    step = StepRecord(step_id=0, prompt="hello", retrieved=[], output="world")
    return TaskTrace(task_id=task_id, task_type="qa", metadata={}, steps=[step])


def test_store_and_retrieve() -> None:
    manager = MemoryManager()
    manager.store_trace("1", _make_trace("1"))
    results = manager.retrieve("hello")
    assert len(results) == 1
    assert results[0].task_id == "1"


def test_sample_for_replay() -> None:
    manager = MemoryManager()
    for i in range(3):
        manager.store_trace(str(i), _make_trace(str(i)))
    samples = manager.sample_for_replay(n=2)
    assert len(samples) == 2


def test_prune_old_data() -> None:
    manager = MemoryManager()
    manager.store_trace("old", _make_trace("old"))
    cutoff = datetime.utcnow() + timedelta(seconds=1)
    manager.prune_old_data(cutoff)
    assert len(manager.bank.get_entries()) == 0
