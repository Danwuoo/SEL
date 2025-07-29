import torch
from sel.cit.loss import compute_loss


def test_compute_loss():
    pred = torch.tensor([1.0, 2.0])
    target = torch.tensor([1.0, 2.0])
    assert compute_loss(pred, target).item() == 0.0
