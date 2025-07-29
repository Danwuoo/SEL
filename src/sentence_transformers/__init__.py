import numpy as np


class SentenceTransformer:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    def encode(
        self,
        texts,
        show_progress_bar: bool = False,
        convert_to_numpy: bool = True,
        normalize_embeddings: bool = True,
    ):
        vecs = np.array([[float(len(t))] for t in texts], dtype=np.float32)
        if normalize_embeddings:
            denom = np.linalg.norm(vecs, axis=1, keepdims=True)
            denom[denom == 0] = 1.0
            vecs = vecs / denom
        return vecs
