import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

#   Amplituden berechen
"""
Um die Amplitude zu berechnen, müssen alle Werte mit e^(Q/10) multipliziert werden, wobei Q
die Verstärkung ist. Die Rechnungen sind ebendiese Rechnungen.
Die Zahl hinter der Variable ist immer die Kennzeichnung des Zylinders!
"""

# amplituden1 = np.array([0.78, 0.48, 1.0, 0.21]) #Arrays mit diesem doofen Wert
# tiefe1 = np.array([41.2, 62.9, 83.0, 121.3])


amplituden = np.array([0.78, 0.48, 0.21]) #Arrays ohne diesen miesen Wert
tiefe = np.array([41.2, 62.9, 121.3])


amplituden[1] *= np.exp(14.8/10)
amplituden[2] *= np.exp(28.75/10)



def f(x, m, b):
    return (m*x + b) 



x = np.linspace(40,125, 1000)
params, pcov = op.curve_fit(f, tiefe, amplituden)
errors = np.sqrt(np.diag(pcov))

plt.plot(tiefe, amplituden, ".", color="mediumblue", label="Messwerte")
plt.plot(x, f(x, *params), color="r", label="Lineare Regression")

plt.legend(loc="best")
plt.xlabel(r'Tiefe / \si{\mm}')
plt.ylabel(r'Amplitude / $\si{\volt}')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

np.round(amplituden, 3)
print("Amplituden nach Verstärkung: ", amplituden)
print("Parameter Regression(m,b): ", np.round(params,4), errors)
