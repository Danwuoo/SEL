from sel.refinement.critic import critique


def test_critique():
    assert critique('draft', 'draft') == 'Needs more detail.'
    assert critique('changed', 'draft') == 'Looks good.'
