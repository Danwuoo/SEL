from sel.rat.retriever import retrieve


def test_retrieve():
    assert retrieve('hi') == 'retrieved: hi'
