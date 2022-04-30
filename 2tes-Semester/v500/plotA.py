from http.client import UnknownProtocol
from operator import ior
import matplotlib.pyplot as plt
import numpy as np

uwerte, iwerte = np.genfromtxt('data/AufgabeA.txt', unpack = True)

uorange = uwerte[:7]
iworange = iwerte[:7]
iorange = np.sqrt(iworange)

ugruen = uwerte[7:20]
iwgruen = iwerte[7:20]
igruen = np.sqrt(iwgruen)

ublau = uwerte[20:41]
iwblau = iwerte[20:41]
iblau = np.sqrt(iwblau)

uviolett = uwerte[41:63]
iwviolett = iwerte[41:63]
iviolett = np.sqrt(iwviolett)

urot = uwerte[63:]
irot = iwerte[63:]

def linregress(x, y):
    N = len(y)
    Delta = N * np.sum(x**2) - (np.sum(x))**2
    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta
    sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))
    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)
    print(A, A_error, B, B_error)

    return A*x + B

plt.clf()
plt.plot(uorange, iorange, 'x', label = 'Messwerte orange')
plt.plot(uorange, linregress(uorange, iorange), 'r', label = 'lineare Regression')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I} \,/\, \sqrt{nA}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/orange.pdf')

plt.clf()
plt.plot(ugruen, igruen, 'x', label = 'Messwerte gruen')
plt.plot(ugruen, linregress(ugruen, igruen), 'r', label = 'lineare Regression')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I} \,/\, \sqrt{nA}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/gruen.pdf')

plt.clf()
plt.plot(ublau, iblau, 'x', label = 'Messwerte blau')
plt.plot(ublau, linregress(ublau, iblau), 'r', label = 'lineare Regression')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I} \,/\, \sqrt{nA}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/blau.pdf')

plt.clf()
plt.plot(uviolett, iviolett, 'x', label = 'Messwerte violett')
plt.plot(uviolett, linregress(uviolett, iviolett), 'r', label = 'lineare Regression')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I} \,/\, \sqrt{nA}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/violett.pdf')

plt.clf()
plt.plot(urot, irot, 'x', label = 'Messwerte rot')
plt.plot(urot, linregress(urot, irot), 'r', label = 'lineare Regression')
plt.xlabel(r'$U \,/\, V$')
plt.ylabel(r'$\sqrt{I} \,/\, \sqrt{nA}$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/rot.pdf')

x = np.array([462, 519, 556, 612, 690])
y = np.array([0.40, 0.56, 0.69, 1.17, 1.38])

plt.clf()
plt.plot(x, y, 'x', label = 'Gegenspannungen')
plt.plot(x, linregress(x, y), 'r', label = 'lineare Regression')
plt.xlabel(r'$\nu \,/\, 10^{12} Hz$')
plt.ylabel(r'$U \,/\, V$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/gegenspannung.pdf')