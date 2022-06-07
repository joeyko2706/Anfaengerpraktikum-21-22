import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


U, I, z = np.genfromtxt("data/ersterStoff.txt", unpack = True)

n = np.sqrt(z)
# n = np.round_(n)

def linregress(x, y):
    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2
    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta
    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))
    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)
    # print(A, A_error, B, B_error)

    return A*x + B

# print(z[10], z[24])

plt.errorbar(U, z, yerr = n, fmt = "gx", label = 'Messwerte')
plt.plot(U[10:25], linregress(U[10:25], z[10:25]), color = "k" , label = 'lineare Regression')
plt.xlabel(r'U $[V]$')
plt.ylabel(r'N [Imp$/120s$]')
plt.grid()
plt.legend()
plt.tight_layout()
#plt.show()

plt.savefig("build/plot.pdf")
#print(U[19], '& $', z[19], '\pm', n[19], '$', '\\', '\\')
# i = 0
# while i < 19:
#     print(U[i], '& $', z[i], '\pm', n[i], '$ &', U[20 + i], '& $', z[20 + i], '\pm', n[20 + i], '\\', '\\')
#     i += 1
# 320 & $9000 \pm 100$ & 500 & $9500 \pm 120$ \\

# e = 1.602 * 10 ** (-19)
# i1 = ufloat(0.2, 0.05)
# i2 = ufloat(0.3, 0.05)
# i3 = ufloat(0.4, 0.05)
# i4 = ufloat(0.5, 0.05)
# i5 = ufloat(0.6, 0.05)
# i6 = ufloat(0.7, 0.05)
# n1 = ufloat(12320, 111)
# n2 = ufloat(12440, 112)
# n3 = ufloat(12626, 112)
# n4 = ufloat(12695, 113)
# n5 = ufloat(13033, 114)
# n6 = ufloat(13219, 115)

# print(i1 * 10 ** (-6) / (e * (n1 / 120)))
# print(i2 * 10 ** (-6) / (e * (n2 / 120)))
# print(i3 * 10 ** (-6) / (e * (n3 / 120)))
# print(i4 * 10 ** (-6) / (e * (n4 / 120)))
# print(i5 * 10 ** (-6) / (e * (n5 / 120)))
# print(i6 * 10 ** (-6) / (e * (n6 / 120)))

# n1 = ufloat(19344, 139)
# n12 = ufloat(34387, 185)
# n2 = ufloat(15400, 124)
# x = (n1 + n2 - n12) / (2 * n1 * n2)
# print(x)