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

print("Sättigungsstrom 10,35 Watt: ", I2a[-1])
print("Sättigungsstrom 8,1 Watt: ", I3a[-1])
print("Sättigungsstrom 7,0 Watt: ", I4a[-1])
print("Sättigungsstrom 5,7 Watt: ", I5a[-1])

#Plots für die erste Aufgabe erstellen


def schoenerPlot():
    plt.xlabel(r'$U \,/\, \si{\volt}$')
    plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
    plt.grid()
    plt.legend()
    plt.tight_layout()


plt.plot(U2a, I2a, ".", color="darkorange", markersize=3, label = r'$P=\SI{10,35}{\watt}$')
plt.plot(U3a, I3a, "g.", markersize=3, label = r'$P=\SI{8,1}{\watt}$')#Plots der drei geringsten Leistungen
plt.hlines(0.284, 90, 115, alpha=0.5, linewidth=1, color = "g")
plt.plot(U4a, I4a, "r.", markersize=3, label = r'$P=\SI{7,0}{\watt}$')
plt.hlines(0.110, 50, 70, alpha=0.5, linewidth=1, color = "r")
plt.plot(U5a, I5a, "m.", markersize=3, label = r'$P=\SI{5,7}{\watt}$')
plt.hlines(0.047, 26, 48, alpha=0.5, linewidth=1, color="m")

schoenerPlot()
plt.savefig("build/plot1.pdf")
plt.clf()
print("Plot 1/4")

#Plot für die beiden höchsten Leistung, bei dem der Sättigungsstrom nicht erreicht wurde



def g(x,a,b,c,d):
    return (a*x**3 +b*x**2+c*x+d)


#Funktion, um den Wendepunkt zu berechnen. Man braucht zwar nur a und b. Wenn man aber alle übergibt, kann man einfach "*params" übergeben
def wendepunkt(a,b,c,d): 
    return (-(2*b)/(6*a))

#Erste Messwerte

x1 = np.linspace(0,250,1000)
x2 = np.linspace(0,180,1000)

params, pcov = op.curve_fit(g, U1a, I1a)
errors = np.sqrt(np.diag(pcov))

print("Paramater Regression bei 13,75 Watt (a,b,c,d): ", params, errors)
print("Wendepunkt 13,75 Watt: ", np.round(wendepunkt(*params),4), np.round(g(wendepunkt(*params), *params),4))
print("Sättigungsstrom bei 13,75 Watt: ", 2*np.round(wendepunkt(*params),4), 2*np.round(g(wendepunkt(*params), *params),4))

plt.plot(x1, g(x1, *params), color="r", label="Regression 3.Grades")
plt.plot(U1a, I1a, "b.", markersize=4, label = r'$P=\SI{13,75}{\watt}$') 
plt.plot(wendepunkt(*params), g(wendepunkt(*params), *params), "kx")


#Zweite Messwerte
params, pcov = op.curve_fit(g, U2a, I2a)
errors = np.sqrt(np.diag(pcov))
print("Paramater Regression bei 10,35 Watt (a,b,c,d): ", params, errors)
print("Wendepunkt 2: ", np.round(wendepunkt(*params),4), np.round(g(wendepunkt(*params), *params),4))
print("Sättigungsstrom bei 10,35 Watt: ", 2*np.round(wendepunkt(*params),4), 2*np.round(g(wendepunkt(*params), *params),4))


plt.plot(x2, g(x2, *params), color="g", label="Regression 3.Grades")
plt.plot(U2a, I2a, ".", color="darkorange", markersize=4, label = r'$P=\SI{10,35}{\watt}$')
plt.hlines(1.178, 170, 190, alpha=0.5, linewidth=1, color="darkorange")
plt.plot(wendepunkt(*params), g(wendepunkt(*params), *params), "kx", label="Wendepunkte")


schoenerPlot()
plt.savefig("build/plot2.pdf")
plt.clf()
print("Plot 2/4")

#Plots für die zweite Aufgabe erstellen
#Gültigkeitsbereich oder der shit der das war suchen ka


def f(x, m, b):
    return (m*x + b) 

U_log = np.log(U1a[1:])
I_log = np.log(I1a[1:])

params, pcov = op.curve_fit(f, U_log, I_log)
errors = np.sqrt(np.diag(pcov))
x3 = np.linspace(1,6,1000)

plt.plot(x3, f(x3, *params), color="r", label="Lineare Regression")
plt.plot(U_log, I_log, "x", color="b" , alpha=0.7, label = r'Messwerte')
print("Parameter Regression fuer Gueltigkeitsbereich (m,b): ", np.round(params,4), errors)

plt.legend()
plt.xlim(1,6)
plt.ylim(f(1, *params), f(6, *params))
plt.xlabel(r'$\log\left(\frac{U}{U_0}\right)')
plt.ylabel(r'$\log\left(\frac{I}{I_0}\right)')
plt.tight_layout()
plt.savefig("build/plot3.pdf")
plt.clf()
print("Plot 3/4")

# Aufgabenteil b)
#Anlaufstromgebiet halblogarithmisch darstellen

U2 = U2 + 1000 * I2 *10**(-9)
x4 = np.linspace(0,1,1000)

#Der Strom muss zunächst noch mit den richtigen Faktoren korrigiert werden

I2[:9] *= 30 * 10**(-9)
I2[9:15] *= 10 * 10**(-9)
I2[15:18] *= 3 * 10**(-9)
I2[18:] *= 10**(-9)
Ilog = np.log(I2)

params, pcov = op.curve_fit(f, U2, Ilog)
errors = np.sqrt(np.diag(pcov))
print("Parameter Regression fuer Anlaufstromgebiet (m,b): ", np.round(params,4), errors)

plt.plot(x4, f(x4, *params), color="r", label="Lineare Regression")
plt.plot(U2, Ilog, 'b.', label="Messwerte")

plt.legend()
plt.grid()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$\log\left(\frac{I}{I_0}\right)')
plt.tight_layout()
plt.savefig("build/plot4.pdf")
print("Plot 4/4")


#Die Latex Tabellen mithilfe von Python ausgeben lassen

# I2 *= 10**9
# n = I2.size
# for i in range(n):
    # print(n.round(U1a[i],4), " & ", np.round(I1a[i],4), ";")
    # print(n.round(U2a[i],4), " & ", np.round(I2a[i],4), ";")
    # print(n.round(U3a[i],4), " & ", np.round(I3a[i],4), ";")
    # print(n.round(U4a[i],4), " & ", np.round(I4a[i],4), ";")
    # print(n.round(U5a[i],4), " & ", np.round(I5a[i],4), ";")
    # print(np.round(U2[i],4), " & ", np.round(I2[i]), ";")   #Aufgabe 2)
    # i +=1