import numpy as np
import matplotlib.pyplot as plt
#from suiteSn import suiteSn

a = np.full((6, 1), 1)
b = np.arange(1, 7)
c = a.reshape(1, 6)
d = 111 * c
I = np.identity(6)
J = np.full((6, 6), 1)
K = np.diag(b)
L = (55*I) - J + (2*(a@c))
M = K; M[:, 0] = a.reshape(6,)
dd = np.linalg.det(M)
x = np.linalg.solve(M, a)
N = np.linalg.solve(M, M.T)

print('\na =\n')
print(a)
print('\nb =\n')
print(b)
print('\nc =\n')
print(c)
print('\nd =\n')
print(d)
print('\nI =\n')
print(I)
print('\nJ =\n')
print(J)
print('\nK =\n')
print(K)
print('\nL =\n')
print(L)
print('\nM =\n')
print(M)
print('\ndd =\n')
print(dd)
print('\nx =\n')
print(x)
print('\nN =\n')
print(N)


plt.matshow(N, cmap='Greens')
plt.title("Figure 1 \n Matrice N", fontsize = 20, color = 'magenta')
plt.figure(1)
plt.show()

#f = ((-x**2)/2) + (np.e)**x + np.sin(x)

x = np.linspace(0, 1, 101)

def fonction(x):
    f = ((-x**2)/2) + (np.e)**x + np.sin(x)
    return f
plt.figure(2)
plt.plot(x,fonction(x))
plt.title("Figure 2 \n Fonction f(x)", fontsize = 20, color = 'brown')
plt.show()

#3
