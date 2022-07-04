import matplotlib.pyplot as plt
import numpy as np


tm = np.array([12.0, 17.8, 23.6, 29.5, 34.9, 40.4, 45.8])
t = tm # * 10 ** (-6)
sm = np.array([14.5, 22.6, 30.5, 38.6, 45.8, 53.7, 61.2])
s = 2 * sm * 10 ** (-3)


def linregress(x, y):
    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2
    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta
    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))
    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)
    print(A, A_error, B, B_error)
    print(A * 10 ** (6), A_error * 10 ** (6), B , B_error)

    return A*x + B

plt.plot(t, s, 'x', label='Messwerte')
plt.plot(t, linregress(t, s), label='lineare Regression')
plt.xlabel(r'$t/\unit{\micro\second}$')
plt.ylabel(r'$s/\unit{\meter}$')
plt.legend()
plt.grid()
plt.savefig('build/plot.pdf')
#plt.show()



# x = np.linspace(0, 10, 1000)
# y = x ** np.sin(x)

# plt.subplot(1, 2, 1)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
# plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
# plt.legend(loc='best')

# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
# plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
# plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot.pdf')
