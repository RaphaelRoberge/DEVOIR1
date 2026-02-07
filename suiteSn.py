import numpy as np

def suiteSn(n):
    S = np.array([np.e-1])

    for i in range(1, n+1):
        Si = np.e - i * S[i-1]
        S = np.append(S, Si)
    return S

test18 = suiteSn(18)
print(test18)

test19 = suiteSn(19)
print(test19)

#testsara