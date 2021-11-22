import numpy as np


def expon(l: float) -> float:
    return -(1/l)*np.log(1-np.random.random())


def uni(lo: int, hi: int) -> float:
    return lo+(hi-lo)*np.random.random()
