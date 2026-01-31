import numpy as np
from math import e

def suiteSn(n):
    S = np.array([np.e-1])

    for i in range(1, n+1):
        Si = np.e - i * S[i-1]
        S = np.append(S, Si)
    return S