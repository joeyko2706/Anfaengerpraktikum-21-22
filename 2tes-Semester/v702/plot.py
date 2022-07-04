import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat

t1, N1 = np.genfromtxt('data/AufgabeA.txt', unpack = True)
t2, N2 = np.genfromtxt('data/AufgabeB.txt', unpack = True)

N1 = N1 - 9
N2 = N2 - 2

t1 = 30 * t1
t2 = 8 * t2
t1 = t1.astype(int)
t2 = t2.astype(int)

wN1 = np.sqrt(N1)
wN1 = np.round_(wN1)
wN1 = wN1.astype(int)
N1 = N1.astype(int)
wN2 = np.sqrt(N2)
wN2 = np.round_(wN2)
wN2 = wN2.astype(int)
N2 = N2.astype(int)

params, covariance_matrix = np.polyfit(t1, np.log(unp.nominal_values(N1)), deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value} ± {error}')


plt.plot(t1, N1, 'x', label='Messwerte')
plt.plot(t1, np.exp(params[0] * t1 + params[1]), label='Lineare Regression', linewidth=3)
plt.errorbar(t1, unp.nominal_values(N1), unp.std_devs(N1), fmt='bx')
plt.legend(loc='best')
plt.yscale('log')
plt.grid()
plt.xlabel(r'$t/\unit{\second}$')
plt.ylabel(r'$N$')
plt.savefig('build/plot1.pdf')
plt.close()


ta = t2[:11]
tb = t2[12:]
Nkorr = 134 * (1-np.exp(-51.90e-4*10))*np.exp(-51.90e-4*ta)
Na = N2[:11] - Nkorr
Nb = N2[12:]

paramsa, covariance_matrixa = np.polyfit(ta, np.log(unp.nominal_values(Na)), deg=1, cov=True)
errorsa = np.sqrt(np.diag(covariance_matrixa))

for name, value, error in zip('ab', paramsa, errorsa):
    print(f'{name} = {value} ± {error}')

paramsb, covariance_matrixb = np.polyfit(tb, np.log(unp.nominal_values(Nb)), deg=1, cov=True)
errorsb = np.sqrt(np.diag(covariance_matrixb))

for name, value, error in zip('ab', paramsb, errorsb):
    print(f'{name} = {value} ± {error}')



plt.plot(t2, N2, 'x', label='Messwerte')
plt.plot(ta, np.exp(paramsa[0] * ta + paramsa[1]), label='Lineare Regression', linewidth=3)
plt.plot(tb, np.exp(paramsb[0] * tb + paramsb[1]), label='Lineare Regression', linewidth=3)
plt.errorbar(t2, unp.nominal_values(N2), unp.std_devs(N2), fmt='bx')
plt.vlines(96, 0, 120, 'r', 'dashed')
plt.legend(loc='best')
plt.yscale('log')
plt.grid()
plt.xlabel(r'$t/\unit{\second}$')
plt.ylabel(r'$N$')
plt.savefig('build/plot2.pdf')
#plt.show()
plt.close()













# for i in range(53):
#     print(t2[i], ' & ', N2[i], ' $ \pm $ ', wN2[i], ' \\','\\')


# lamb = ufloat(-0.005190, 0.000883)
# print(np.log(2)/lamb)


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

# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot.pdf')
