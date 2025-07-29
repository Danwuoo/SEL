from sel.agentic import Agent, AgenticController, EchoEnv


def test_agent_episode():
    agent = Agent()
    controller = AgenticController(agent)
    trace = controller.run_episode({}, EchoEnv())
    assert trace["steps"][0]["action"] == "start"
