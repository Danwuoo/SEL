from sel.meta.metrics import accuracy


def test_accuracy():
    assert accuracy(1, 1) == 1.0
    assert accuracy(0, 1) == 0.0
