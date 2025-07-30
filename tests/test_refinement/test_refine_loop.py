from sel.refinement.refine_loop import run_refinement


def test_run_refinement_single_round():
    result = run_refinement('hello', max_rounds=1)
    trace = result['trace']
    assert trace.steps[0].version == 0
    assert trace.steps[0].feedback == 'Needs more detail.'
    assert result['refined_output'].startswith('hello')
