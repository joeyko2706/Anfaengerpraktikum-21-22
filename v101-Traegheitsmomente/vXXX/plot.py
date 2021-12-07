import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0, 10, 1000)
#y = x ** np.sin(x)

#plt.subplot(1, 2, 1)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)


x = np.linspace(60, 240, 10)
y = [3.08, 3.40, 3.83, 4.32, 4.83, 5.37, 5.76, 6.28, 6.84, 7.36]

N = len(y)
Delta = N * np.sum(x**2) - (np.sum(x))**2

A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

A_error = sigma_y * np.sqrt(N / Delta)
B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

#xn = x*x
#yn = y**2
plt.plot(x, y, 'b.', label='Messwerte')
plt.xlabel(r'Abstand $a$ / mm')
plt.ylabel(r'$T$ / s')


plt.plot(x, A*x + B, 'r', label='lineare Regression')

plt.grid()
plt.legend()
print(A, A_error, B, B_error)

plt.savefig('build/plot.pdf')
