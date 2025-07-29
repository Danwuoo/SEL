from sel.agentic.controller import AgenticLoopController
from sel.agentic.agent import BaseAgent
from sel.agentic.interface import TaskEnvironment, TaskInput


class SimpleAgent(BaseAgent):
    def decide(self, context: str) -> str:
        return f"decide:{context}"


class SimpleEnv(TaskEnvironment):
    def present_task(self, task_input: TaskInput) -> dict:
        return {"context": task_input.prompt}

    def get_feedback(self, output: str) -> dict:
        ctx = output.split(":", 1)[-1]
        return {"feedback": ctx[::-1]}


def test_run_episode():
    agent = SimpleAgent()
    env = SimpleEnv()
    controller = AgenticLoopController(agent, env)
    trace = controller.run_episode(TaskInput(prompt="hi"))
    assert trace.rounds
    step = trace.rounds[0]
    assert step.decision == "decide:hi"
    assert step.feedback["feedback"] == "ih"  # reversed
