from sel.refinement.scorer import score


def test_score_similarity():
    assert score('a', 'a') == 1.0
    assert score('a', 'b') < 1.0
