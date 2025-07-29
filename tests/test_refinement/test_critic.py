from sel.refinement.critic import critique


def test_critique():
    assert critique('foo') == 'critic: foo'
