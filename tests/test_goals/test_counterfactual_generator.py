from sel.goals.counterfactual import generate
from sel.logging.trace_schema import StepRecord, TaskTrace


def test_generate_counterfactual() -> None:
    trace = TaskTrace(
        task_id="t1",
        task_type="qa",
        metadata={"context": "math"},
        steps=[StepRecord(step_id=0, prompt="What is 2+2?", retrieved=[], output="5")],
        result={"success": False},
    )

    cf_task = generate(trace)
    assert cf_task.origin_task_id == "t1"
    assert "detail" in cf_task.modified_prompt
