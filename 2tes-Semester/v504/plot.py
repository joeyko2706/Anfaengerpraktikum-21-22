import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties import ufloat

print("Plots werden erstellt")
#Daten aus Textdateien importieren

U1a, I1a = np.genfromtxt("data/Aufgabe1a.txt", unpack=True)
U2a, I2a = np.genfromtxt("data/Aufgabe1b.txt", unpack=True)
U3a, I3a = np.genfromtxt("data/Aufgabe1c.txt", unpack=True)
U4a, I4a = np.genfromtxt("data/Aufgabe1d.txt", unpack=True)
U5a, I5a = np.genfromtxt("data/Aufgabe1e.txt", unpack=True)
U2, I2 = np.genfromtxt("data/Aufgabe2.txt", unpack=True)

plt.plot(U1a, I1a, ".", markersize=3, label = r'$P=\SI{13,75}{\watt}$')
plt.plot(U2a, I2a, ".", markersize=3, label = r'$P=\SI{10,35}{\watt}$')
plt.plot(U3a, I3a, ".", markersize=3, label = r'$P=\SI{8,1}{\watt}$')
plt.plot(U4a, I4a, ".", markersize=3, label = r'$P=\SI{7,0}{\watt}$')
plt.plot(U5a, I5a, ".", markersize=3, label = r'$P=\SI{5,7}{\watt}$')

plt.legend()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
plt.tight_layout()
plt.savefig("build/plot1.pdf")
plt.clf()
print("Plot 1/3")

plt.plot(U1a[:12], I1a[:12], ".", markersize=3, label = r'$P=\SI{13,75}{\watt}$')
plt.plot(U2a[:12], I2a[:12], ".", markersize=3, label = r'$P=\SI{10,35}{\watt}$')
plt.plot(U3a[:12], I3a[:12], ".", markersize=3, label = r'$P=\SI{8,1}{\watt}$')
plt.plot(U4a[:12], I4a[:12], ".", markersize=3, label = r'$P=\SI{7,0}{\watt}$')
plt.plot(U5a[:12], I5a[:12], ".", markersize=3, label = r'$P=\SI{5,7}{\watt}$')

plt.legend()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
plt.tight_layout()
plt.savefig("build/plot2.pdf")
plt.clf()
print("Plot 2/3")

# Aufgabenteil b)


def f(x, m, b):
    return (m*x + b) 


U2 = U2 + 1000 * I2 *10**(-9)
x = np.linspace(0,1,1000)

#Der Strom muss zunächst noch mit den richtigen Faktoren korrigiert werden

I2[:9] *= 30 * 10**(-9)
I2[9:15] *= 10 * 10**(-9)
I2[15:18] *= 3 * 10**(-9)
I2[18:] *= 10**(-9)
Ilog = np.log(I2)

params, pcov = op.curve_fit(f, U2, Ilog)
errors = np.sqrt(np.diag(pcov))

plt.plot(x, f(x, *params), label="Lineare Regression")
plt.plot(U2, Ilog, '.', label="Messwerte")

plt.legend()
plt.grid()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$\log\left(\frac{I}{I_0}\right)')
plt.tight_layout()
plt.savefig("build/plot3.pdf")
print("Plot 3/3")


#Die Latex Tabellen mithilfe von Python ausgeben lassen

I2 *= 10**9
n = I2.size
for i in range(n):
    print(np.round(U2[i],4), " & ", np.round(I2[i]), ";")   #Aufgabe 2)
    i +=1