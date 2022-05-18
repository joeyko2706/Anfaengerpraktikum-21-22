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

#Plots für die erste Aufgabe erstellen

plt.plot(U3a, I3a, "g.", markersize=3, label = r'$P=\SI{8,1}{\watt}$')#Plots der drei geringsten Leistungen
plt.hlines(0.284, 90, 115, linestyle = "dashed", linewidth=1, color = "g")
plt.plot(U4a, I4a, "r.", markersize=3, label = r'$P=\SI{7,0}{\watt}$')
plt.hlines(0.110, 50, 70, linestyle = "dashed", linewidth=1, color = "r")
plt.plot(U5a, I5a, "m.", markersize=3, label = r'$P=\SI{5,7}{\watt}$')
plt.hlines(0.047, 26, 48, linestyle = "dashed", linewidth=1, color="m")

plt.legend()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
plt.tight_layout()
plt.savefig("build/plot1.pdf")
plt.clf()
print("Plot 1/4")

#Plot für die beiden höchsten Leistung, bei dem der Sättigungsstrom nicht erreicht wurde


def g(x,a,b,c,d):
    return (a*x**3 +b*x**2+c*x+d)


params, pcov = op.curve_fit(g, U1a, I1a)
errors = np.sqrt(np.diag(pcov))
x1 = np.linspace(0,250,1000)
x2 = np.linspace(0,180,1000)

plt.plot(x1, g(x1, *params), color="r", label="Fit")
plt.plot(U1a, I1a, "b.", markersize=4, label = r'$P=\SI{13,75}{\watt}$') 


params, pcov = op.curve_fit(g, U2a, I2a)
errors = np.sqrt(np.diag(pcov))
plt.plot(x2, g(x2, *params), color="darkorange", label="Fit")
plt.plot(U2a, I2a, "g.", markersize=4, label = r'$P=\SI{10,35}{\watt}$')


plt.legend()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
plt.tight_layout()
plt.savefig("build/plot2.pdf")
plt.clf()
print("Plot 2/4")

#Plots für die zweite Aufgabe erstellen

plt.plot(U1a[:12], I1a[:12], ".", markersize=3, label = r'$P=\SI{13,75}{\watt}$')
plt.plot(U2a[:12], I2a[:12], ".", markersize=3, label = r'$P=\SI{10,35}{\watt}$')
plt.plot(U3a[:12], I3a[:12], ".", markersize=3, label = r'$P=\SI{8,1}{\watt}$')
plt.plot(U4a[:12], I4a[:12], ".", markersize=3, label = r'$P=\SI{7,0}{\watt}$')
plt.plot(U5a[:12], I5a[:12], "m.", markersize=3, label = r'$P=\SI{5,7}{\watt}$')

plt.legend()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
plt.tight_layout()
plt.savefig("build/plot3.pdf")
plt.clf()
print("Plot 3/4")

# Aufgabenteil b)


def f(x, m, b):
    return (m*x + b) 


U2 = U2 + 1000 * I2 *10**(-9)
x3 = np.linspace(0,1,1000)

#Der Strom muss zunächst noch mit den richtigen Faktoren korrigiert werden

I2[:9] *= 30 * 10**(-9)
I2[9:15] *= 10 * 10**(-9)
I2[15:18] *= 3 * 10**(-9)
I2[18:] *= 10**(-9)
Ilog = np.log(I2)

params, pcov = op.curve_fit(f, U2, Ilog)
errors = np.sqrt(np.diag(pcov))

plt.plot(x3, f(x3, *params), label="Lineare Regression")
plt.plot(U2, Ilog, '.', label="Messwerte")

plt.legend()
plt.grid()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$\log\left(\frac{I}{I_0}\right)')
plt.tight_layout()
plt.savefig("build/plot4.pdf")
print("Plot 4/4")


#Die Latex Tabellen mithilfe von Python ausgeben lassen

I2 *= 10**9
n = I2.size
for i in range(n):
    print(np.round(U2[i],4), " & ", np.round(I2[i]), ";")   #Aufgabe 2)
    i +=1