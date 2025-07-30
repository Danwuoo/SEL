from sel.critic import LlmCritic, RuleBasedCritic


def test_llm_critic():
    critic = LlmCritic()
    result = critic.critique("draft", "draft")
    assert not result.valid
    assert result.summary == "Needs more detail."


def test_rule_based_critic():
    critic = RuleBasedCritic()
    result = critic.critique("code", "def foo():\n    pass")
    assert not result.valid
    assert "incomplete" in result.error_types
