import matplotlib.pyplot as plt
import numpy as np


print(r'Plots werden durchgegangen')

f, U = np.genfromtxt('a.txt', unpack = True)
U *= 10**(-3)

plt.plot(f, U, '.' ,color = 'mediumblue', label = 'Messwerte')
plt.xlabel(r'$\nu$ / kHz')
plt.ylabel(r'$U_A$ / mV')
plt.legend(loc='upper left')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
