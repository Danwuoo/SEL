class Tensor(list):
    def __init__(self, data):
        super().__init__(float(x) for x in data)

    def __sub__(self, other):
        return Tensor([a - b for a, b in zip(self, other)])

    def __pow__(self, exponent):
        return Tensor([x ** exponent for x in self])

    def __truediv__(self, other):
        return Tensor([x / other for x in self])

    def mean(self):
        return Tensor([sum(self) / len(self)])

    def item(self):
        return self[0] if self else 0.0

def tensor(data):
    return Tensor(data)
