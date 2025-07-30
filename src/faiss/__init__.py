import numpy as np


class IndexFlatIP:
    def __init__(self, dim: int):
        self.vectors = np.empty((0, dim), dtype=np.float32)

    @property
    def ntotal(self) -> int:
        return len(self.vectors)

    def add(self, vecs: np.ndarray) -> None:
        self.vectors = np.vstack([self.vectors, vecs])

    def search(self, query: np.ndarray, k: int):
        # Use negative L2 distance as a similarity metric for determinism
        diff = query[:, None, :] - self.vectors[None, :, :]
        scores = -np.linalg.norm(diff, axis=2)
        idx = np.argsort(-scores, axis=1)[:, :k]
        sorted_scores = np.take_along_axis(scores, idx, axis=1)
        return sorted_scores, idx


def write_index(index: IndexFlatIP, path: str) -> None:
    with open(path, "wb") as f:
        np.save(f, index.vectors)


def read_index(path: str) -> IndexFlatIP:
    with open(path, "rb") as f:
        vecs = np.load(f)
    index = IndexFlatIP(vecs.shape[1])
    index.vectors = vecs
    return index
