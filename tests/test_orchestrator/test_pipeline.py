from sel.orchestrator.pipeline import run_pipeline


def test_run_pipeline(capsys):
    run_pipeline()
    captured = capsys.readouterr()
    assert 'pipeline running' in captured.out
