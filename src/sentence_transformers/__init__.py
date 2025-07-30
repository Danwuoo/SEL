import numpy as np


class SentenceTransformer:
    def __init__(self, model_name: str = 'dummy') -> None:
        self.model_name = model_name

    def encode(
        self,
        texts,
        show_progress_bar: bool = False,
        convert_to_numpy: bool = True,
        normalize_embeddings: bool = True,
    ):
        vecs = np.array([[float(abs(hash(t)) % 1000)] for t in texts], dtype='float32')
        if normalize_embeddings:
            norm = np.linalg.norm(vecs, axis=1, keepdims=True)
            norm[norm == 0] = 1
            vecs = vecs / norm
        return vecs
