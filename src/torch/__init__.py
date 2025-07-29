import numpy as np

Tensor = np.ndarray

def tensor(data):
    return np.array(data, dtype=float)

def mean(x):
    return np.mean(x)
