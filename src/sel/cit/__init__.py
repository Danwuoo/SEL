"""Contrastive Instruction Tuning module."""

from .loss import compute_loss, info_nce_loss

try:  # pragma: no cover - optional heavy deps
    from .embedding_model import EmbeddingModel
    from .evaluator import evaluate_similarity
    from .sampler import InstructionPairDataset, collate_batch
    from .trainer import train_cit_loop

    __all__ = [
        "EmbeddingModel",
        "evaluate_similarity",
        "compute_loss",
        "info_nce_loss",
        "InstructionPairDataset",
        "collate_batch",
        "train_cit_loop",
    ]
except Exception:  # pragma: no cover
    __all__ = ["compute_loss", "info_nce_loss"]


