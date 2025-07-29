import numpy as np
import pickle

class IndexFlatIP:
    def __init__(self, dim: int) -> None:
        self.vectors = np.empty((0, dim), dtype=np.float32)

    def add(self, vecs: np.ndarray) -> None:
        self.vectors = np.vstack([self.vectors, vecs])

    @property
    def ntotal(self) -> int:
        return len(self.vectors)

    def search(self, query: np.ndarray, top_k: int):
        if self.ntotal == 0:
            dists = np.zeros((1, top_k), dtype=np.float32)
            idx = -np.ones((1, top_k), dtype=int)
            return dists, idx
        scores = np.dot(query, self.vectors.T)
        idx = np.argsort(-scores, axis=1)[:, :top_k]
        dists = np.take_along_axis(scores, idx, axis=1)
        return dists, idx


def write_index(index: IndexFlatIP, path: str) -> None:
    with open(path, 'wb') as f:
        pickle.dump(index.vectors, f)


def read_index(path: str) -> IndexFlatIP:
    with open(path, 'rb') as f:
        vecs = pickle.load(f)
    idx = IndexFlatIP(vecs.shape[1])
    idx.vectors = vecs
    return idx
