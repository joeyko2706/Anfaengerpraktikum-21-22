import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

ar = ufloat(-1.77, 0.11)
br = ufloat(0.71, 0.03)
ao = ufloat(-2.91, 0.23)
bo = ufloat(1.62, 0.07)
ag = ufloat(-3.35, 0.12)
bg = ufloat(2.31, 0.05)
ab = ufloat(-2.78, 0.08)
bb = ufloat(3.26, 0.05)
av = ufloat(-2.24, 0.07)
bv = ufloat(3.08, 0.05)
print(-br/ar, -bo/ao, -bg/ag, -bb/ab, -bv/av)

ub, ib = np.genfromtxt('data/AufgabeB.txt', unpack = True)

plt.plot(ub, ib, 'x', label = 'Messwerte orange')
plt.xlabel(r'$U / V$')
plt.ylabel(r'$I / nA$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout()
plt.savefig('build/aufgb.pdf')
