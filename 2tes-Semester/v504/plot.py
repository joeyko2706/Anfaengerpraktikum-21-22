import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


print("Plots werden erstellt")
#Daten aus Textdateien importieren

U1a, I1a = np.genfromtxt("data/Aufgabe1a.txt", unpack=True)
U2a, I2a = np.genfromtxt("data/Aufgabe1b.txt", unpack=True)
U3a, I3a = np.genfromtxt("data/Aufgabe1c.txt", unpack=True)
U4a, I4a = np.genfromtxt("data/Aufgabe1d.txt", unpack=True)
U5a, I5a = np.genfromtxt("data/Aufgabe1e.txt", unpack=True)
U2, I2 = np.genfromtxt("data/Aufgabe2.txt", unpack=True)

# print("Sättigungsstrom 10,35 Watt: ", I2a[-1])
# print("Sättigungsstrom 8,1 Watt: ",   I3a[-1])
# print("Sättigungsstrom 7,0 Watt: ",   I4a[-1])
# print("Sättigungsstrom 5,7 Watt: ",   I5a[-1])

#Plots für die erste Aufgabe erstellen


def schoenerPlot():
    plt.xlabel(r'$U \,/\, \si{\volt}$')
    plt.ylabel(r'$I \,/\, \si{\milli\ampere}')
    plt.grid()
    plt.legend()
    plt.tight_layout()


plt.plot(U2a, I2a, ".", color="darkorange", markersize=3, label = r'$P=\SI{10,35}{\watt}$')
plt.plot(U3a, I3a, "g.", markersize=3, label = r'$P_{\text H}=\SI{8,1}{\watt}$')#Plots der drei geringsten Leistungen
plt.hlines(0.284, 90, 115, alpha=0.5, linewidth=1, color = "g")
plt.plot(U4a, I4a, "r.", markersize=3, label = r'$P_{\text H}=\SI{7,0}{\watt}$')
plt.hlines(0.110, 50, 70, alpha=0.5, linewidth=1, color = "r")
plt.plot(U5a, I5a, "m.", markersize=3, label = r'$P_{\text H}=\SI{5,7}{\watt}$')
plt.hlines(0.047, 26, 48, alpha=0.5, linewidth=1, color="m")

schoenerPlot()
plt.savefig("build/plot1.pdf")
plt.clf()
print("Plot 1/4")

#Plot für die beiden höchsten Leistung, bei dem der Sättigungsstrom nicht erreicht wurde



def g(x,a,b,c,d):
    return (a*x**3 +b*x**2+c*x+d)


#Funktion, um den Wendepunkt zu berechnen. Man braucht zwar nur a und b. Wenn man aber alle übergibt, kann man einfach "*params" übergeben
def wendepunkt(a,b): 
    wert =  (-(2*b)/(6*a))
    return wert

#Erste Messwerte

x1 = np.linspace(0,250,1000)
x2 = np.linspace(0,180,1000)

params, pcov = op.curve_fit(g, U1a, I1a)
errors = np.sqrt(np.diag(pcov))
a1 = ufloat(params[0], errors[0])
b1 = ufloat(params[1], errors[1])
c1 = ufloat(params[2], errors[2])
d1 = ufloat(params[3], errors[3])

wp1 = wendepunkt(a1,b1)
y1 = g(wp1, a1, b1, c1, d1)

# print("Paramater Regression bei 13,75 Watt (a,b,c,d): ", a1, b1, c1, d1)
# print("Wendepunkt 13,75 Watt: ", wp1, y1)
# print("Sättigungsstrom bei 13,75 Watt: ", 2*wp1, 2*y1)

plt.plot(x1, g(x1, *params), color="r", label="Regression 3.Grades")
plt.plot(U1a, I1a, "b.", markersize=4, label = r'$P_{\text H}=\SI{13,75}{\watt}$') 
# plt.errorbar(noms(wp1), noms(y1), xerr=stds(wp1), yerr=stds(y1), color="black")
plt.plot(noms(wp1), noms(y1), "kx")


#Zweite Messwerte
params, pcov = op.curve_fit(g, U2a, I2a)
errors = np.sqrt(np.diag(pcov))
a2 = ufloat(params[0], errors[0])
b2 = ufloat(params[1], errors[1])
c2 = ufloat(params[2], errors[2])
d2 = ufloat(params[3], errors[3])
wp2 = wendepunkt(a2,b2)
y2 = g(wp2, a2, b2, c2, d2)

# print("Paramater Regression bei 10,35 Watt (a,b,c,d): ", a2, b2, c2, d2)
# print("Wendepunkt 10,35 Watt: ", wp2, y2)
# print("Sättigungsstrom bei 10,35 Watt: ", 2*wp2, 2*y2)


plt.plot(x2, g(x2, *params), color="g", label="Regression 3.Grades")
plt.plot(U2a, I2a, ".", color="darkorange", markersize=4, label = r'$P_{\text H}=\SI{10,35}{\watt}$')
plt.hlines(1.178, 170, 190, alpha=0.5, linewidth=1, color="darkorange")
# plt.errorbar(noms(wp2), noms(y2), xerr=stds(wp2), yerr=stds(y2), color="black", label="Wendepunkte")
plt.plot(noms(wp2), noms(y2), "kx", label="Wendepunkte")

schoenerPlot()
plt.savefig("build/plot2.pdf")
plt.clf()
print("Plot 2/4")

#Plots für die zweite Aufgabe erstellen
#Gültigkeitsbereich oder der shit der da war ka


def f(x, m, b):
    return (m*x + b) 

U_log = np.log(U1a[1:])
I_log = np.log(I1a[1:])

params, pcov = op.curve_fit(f, U_log, I_log)
errors = np.sqrt(np.diag(pcov))
x3 = np.linspace(1,6,1000)

plt.plot(x3, f(x3, *params), color="r", label="Lineare Regression")
plt.plot(U_log, I_log, "x", color="b" , alpha=0.7, label = r'Messwerte')
# print("Parameter Regression fuer Gueltigkeitsbereich (m,b): ", np.round(params,4), errors)

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
m = ufloat(params[0], errors[0])
b = (params[1], errors[1])
# print("Parameter Regression fuer Anlaufstromgebiet (m,b): ", np.round(params,4), errors)

plt.plot(x4, f(x4, *params), color="r", label="Lineare Regression")
plt.plot(U2, Ilog, 'b.', label="Messwerte")
plt.plot(U2[9], Ilog[9], ".",   color="limegreen")
plt.plot(U2[15], Ilog[15], ".", color="limegreen")
plt.plot(U2[18], Ilog[18], ".", color="limegreen")

plt.legend()
plt.grid()
plt.xlabel(r'$U \,/\, \si{\volt}$')
plt.ylabel(r'$\log\left(\frac{I}{I_0}\right)')
plt.tight_layout()
plt.savefig("build/plot4.pdf")
print("Plot 4/4")

"""
# Im folgenden sind nur Rechnungen, die auskommentiert sind, um Rechenleistung zu sparen dazu einfach die drei Anführungszeichen
# aus den Zeilen 176 und 261 entfernen

#Konstanten festlegen
e = const.elementary_charge
k = const.Boltzmann
eta = 0.28
f = 0.32 *10**(-4)
n_wl = 0.95
sigma = const.sigma
m_0 = const.m_e
h = const.h
phi_lit = 4.55

def kathodentemperatur(x):
    return (-e/(k*x))

kathodeAnlauf = kathodentemperatur(m)
print('Kathode im Anlaufgebiet = (%.3f ± %.3f)' % (noms(kathodeAnlauf), stds(kathodeAnlauf)))

def kathodenZwei(x):
    return ((x-n_wl)/(f*eta*sigma))**(1/4)


P1 = 13.5 #Heizleistungen implementieren und dann die zugehörigen Kathodentemperaturen ausgeben
P2 = 10.35
P3 = 8.1
P4 = 7.0
P5 = 5.7

IS1 = 2*y1*10**(-3)      #Sättigungsströme definieren
IS2 = 2*y2*10**(-3)
IS3 = I3a[-1]*10**(-3)
IS4 = I4a[-1]*10**(-3)
IS5 = I5a[-1] *10**(-3)

ln1 = unp.log(y1)
ln2 = unp.log(y2)

k1 = kathodenZwei(P1)
k2 = kathodenZwei(P2)
k3 = kathodenZwei(P3)
k4 = kathodenZwei(P4)
k5 = kathodenZwei(P5)

print("Kathodentemperaturen pro Leistung (abst.): ", k1)
print("Kathodentemperaturen pro Leistung (abst.): ", k2)
print("Kathodentemperaturen pro Leistung (abst.): ", k3)
print("Kathodentemperaturen pro Leistung (abst.): ", k4)
print("Kathodentemperaturen pro Leistung (abst.): ", k5)


def austrittsArbeit(T, I_s):
    return (-(k*T)/e * np.log((I_s * h**3)/(4 * np.pi*f*e*m_0*k**2*T**2)))


def austrittsArbeit2(T, I_s):
    return (-(k*T)/e * unp.log((I_s * h**3)/(4 * np.pi*f*e*m_0*k**2*T**2)))


arbeit1 = austrittsArbeit2(k1,IS1)
arbeit2 = austrittsArbeit2(k2,IS2)
arbeit3 = austrittsArbeit(k3,IS3)
arbeit4 = austrittsArbeit(k4,IS4)
arbeit5 = austrittsArbeit(k5,IS5)
wert = np.array([arbeit1, arbeit2, arbeit3, arbeit4, arbeit5])
mittelArbeiten = sum(wert)/len(wert)


print("Austrittsarbeit pro Leistung (abst.): ", arbeit1)
print("Austrittsarbeit pro Leistung (abst.): ", arbeit2)
print("Austrittsarbeit pro Leistung (abst.): ", arbeit3)
print("Austrittsarbeit pro Leistung (abst.): ", arbeit4)
print("Austrittsarbeit pro Leistung (abst.): ", arbeit5)
print("Mittelwert Austrittsarbeiten: ", mittelArbeiten)
print("Abweichung vom LitWert Austrtittsarbeit: ", abs((mittelArbeiten-phi_lit)/phi_lit)*100)

m = ufloat(1.437, 0.0146)
print("Abweichung vom LitWert für m: ", ((m-1.5)/1.5)*100)

t1 = ufloat(2865.095, 343.460)
t2 = 2229.3641

print("Abweichung Kathodentemperatur: ", (t1-t2)/t2)
"""