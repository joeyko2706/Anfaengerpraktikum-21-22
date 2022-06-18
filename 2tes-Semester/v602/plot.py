import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

# Konstanten definieren

lichtg = const.c
planck = const.h
d = 201.4 * 10 ** (-12)
e = const.e

# Daten ziehen

theta, Rate = np.genfromtxt("data/Roentgenemission/emission", unpack=True)
thetaBr, RateBr = np.genfromtxt("data/Roentgenemission/brom", unpack=True)
thetaGa, RateGa = np.genfromtxt("data/Roentgenemission/gallium_richtig", unpack=True)
thetaSr, RateSr = np.genfromtxt("data/Roentgenemission/strontium", unpack=True)
thetaZn, RateZn = np.genfromtxt("data/Roentgenemission/zink", unpack=True)
thetaZr, RateZr = np.genfromtxt("data/Roentgenemission/Zirkonium", unpack=True)


# Vorbereitungsaufgabe


def f(E):  # Funktion, um die Energien in der Vorbereitungsaufgabe zu bestimmen
    a = np.arcsin((planck * lichtg) / (2 * d * E * e))
    return np.rad2deg(a)


# print("Winkel Germanium:", f(11114)) #bereits in eV
# print("Winkel Brom:", f(13484))
# print("Winkel Rubidium :", f(15208))
# print("Winkel Strontium :", f(16115))
# print("Winkel Zirconium:", f(18008))
# print("Winkel Gallium:", f(10368))

# Emissionsspektrum


def y(winkel):
    return (planck*lichtg)/(2.0*d*np.sin(winkel*np.pi/180)*e)


def h(Energie, Breite):  # Funktion, um das Auflösevermögen zu bestimmen
    return Energie / Breite


def schoenerPlot():
    plt.legend()
    plt.xlabel(r"$2\vartheta$ / DEG")
    plt.ylabel(r"Zählrate")
    plt.tight_layout(pad=0, h_pad=1.09, w_pad=1.09)
    plt.grid()


alphaMax = Rate[175]  # Peak von Alpha
betaMax = Rate[152]  # Peak von Beta
breiteAlpha = np.round(20.451 - 20.0, 3)  # Halbwertsbreite von der K-Alpha Linie
breiteBeta = np.round(22.71 - 22.29, 3)  # von beta


EnergieAlpha = 8047.823  # Energien der beiden Absorptionskanten in eV
EnergieBeta = 8905.413
EnergieAlphaGemessen = y(22.5)
EnergieBetaGemessen = y(20.2)


# Plots programmieren
# print("Plot 1")


plt.plot(theta, Rate, "b", alpha=0.7)
plt.plot(theta,Rate,"r.",label="Messwerte",markersize=5,markeredgewidth=0.5,markeredgecolor="k",)
plt.plot(theta[175], Rate[175], ".", color="limegreen", label=r"$K_\alpha$-Breite")
plt.plot(theta[152], Rate[152], ".", color="magenta", label=r"$K_\beta$-Breite")
# plt.plot(theta[77], Rate[77], ".", color="dodgerblue", label="Bremsberg")
schoenerPlot()
plt.savefig("build/plot1.pdf")
plt.clf()


plt.plot(theta[140:185], Rate[140:185], "b", alpha=0.7)
plt.plot(theta[140:185],Rate[140:185],"r.",label="Messwerte",markersize=5,markeredgewidth=0.5,markeredgecolor="k",)
plt.plot(theta[175], Rate[175], ".", color="limegreen", label=r"$K_\alpha$-Kante")
plt.plot(theta[152], Rate[152], ".", color="magenta", label=r"$K_\beta$-Kante")

plt.hlines(702.0, 20, 20.451, linewidth=1, color="magenta")  # beta
plt.hlines(2540.0, 22.29, 22.71, linewidth=1, color="limegreen")  # alpha

schoenerPlot()
plt.savefig("build/plot2.pdf")
plt.clf()


# Absorbtionsspektren programmieren


# Brom

plt.plot(thetaBr, RateBr, "b", alpha=0.5)
plt.plot(thetaBr, RateBr, "r.", label="Messwerte des Bromabsorbers")
# plt.vlines(thetaBr[8], RateBr[0], RateBr[8], color="limegreen", label=r"K-Kante")
plt.axvline(thetaBr[8], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig("build/plot3.pdf")
plt.clf()

# Gallium

plt.plot(thetaGa, RateGa, "b", alpha=0.5)
plt.plot(thetaGa, RateGa, "r.", label="Messwerte des Galliumabsorbers")
# plt.vlines(thetaGa[6], RateGa[0], RateGa[6], color="limegreen", label=r"K-Kante")
plt.axvline(thetaGa[9], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig("build/plot4.pdf")
plt.clf()

# Strontium

plt.plot(thetaSr, RateSr, "b", alpha=0.5)
plt.plot(thetaSr, RateSr, "r.", label="Messwerte des Strontiumabsorbers")
# plt.vlines(thetaSr[6], RateSr[0], RateSr[6], color="limegreen", label=r"K-Kante")
plt.axvline(thetaSr[8], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig("build/plot5.pdf")
plt.clf()

# Zink

plt.plot(thetaZn, RateZn, "b", alpha=0.5)
plt.plot(thetaZn, RateZn, "r.", label="Messwerte des Zinkabsorbers")
# plt.vlines(thetaZn[5], RateZn[0], RateZn[5], color="limegreen", label=r"K-Kante")
plt.axvline(thetaZn[7], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig("build/plot6.pdf")
plt.clf()

# Zirkonium

plt.plot(thetaZr, RateZr, "b", alpha=0.5)
plt.plot(thetaZr, RateZr, "r.", label="Messwerte des Zirkoniumabsorbers")
# plt.vlines(thetaZr[5], RateZr[0], RateZr[5], color="limegreen", label=r"K-Kante")
plt.axvline(thetaZr[-1], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig("build/plot7.pdf")
plt.clf()




# Moseley Gesetz:
# Kommen aus den Berechnungen unten, ich wollte aber alle Berchnungen auf einmal ausklammern können, weshalb ich das hier schon implementiert habe
EnergieBrom = 13470.5       
EnergieGallium = 10368.1
EnergieStrontium = 16107.2
EnergieZink =   9660.755
EnergieZirkonium =  17995.872
Ryd = 13.6

E_absorp = np.array([EnergieBrom, EnergieGallium, EnergieStrontium, EnergieZink, EnergieZirkonium])
kernladungen = np.array([35, 31, 38, 30, 40])


def linReg(x,m,b):
    return (m*x+b)


x1 = np.linspace(95, 140, 10000)
params, pcov = op.curve_fit(linReg, np.sqrt(E_absorp), kernladungen)
errors = np.sqrt(np.diag(pcov))

plt.plot(x1, linReg(x1, *params) , 'b', label="Lineare Regression")
plt.plot(np.sqrt(E_absorp), kernladungen, 'r.', label="Messwerte")

plt.legend()
plt.xlim(95,140)
plt.ylim(29,41)
plt.xlabel(r"$\sqrt{E} ~/~ \sqrt{eV}$")
plt.ylabel(r"Z")
plt.tight_layout(pad=0, h_pad=1.09, w_pad=1.09)
plt.grid()
plt.savefig("build/plot8.pdf")
plt.clf()

m = ufloat(np.round(params[0], 4), np.round(errors[0],4))
b = ufloat(np.round(params[1], 4), np.round(errors[0],4))


print(np.sqrt(E_absorp), kernladungen)
print("Parameter linReg (m,b): ", m, b)
E_ryd = 1/(m**2)
print("E_Ryd gemessen: ", E_ryd, "E_Ryd: ", Ryd)
print("Abweichung RydberEnergie: ", (E_ryd-Ryd)/Ryd*100, "%")

# Berechnungen
"""

EnergieAlphaGemessen = 8043.355
EnergieBetaGemessen = 8914.204

print("Maximum Beta: ",theta[152],betaMax,"Halbwertsbreite (y): ",1 / 2 * betaMax,"Breite (x): ",breiteBeta,)
print("Maximum Alpha: ",theta[175],alphaMax,"Halbwertsbreite (y): ",1 / 2 * alphaMax,"Breite (x): ",breiteAlpha,)

print("Energie Alpha: ", EnergieAlphaGemessen)
print("Energie Beta: ", EnergieBetaGemessen)
print("Abweichung von Alpha: ",(EnergieAlphaGemessen - EnergieAlpha) / EnergieAlpha * 100,"%",)
print("Abweichung von Beta: ", (EnergieBetaGemessen - EnergieBeta) / EnergieBeta * 100, "%",)
print("Auflösevermögen Alpha: ", h(EnergieAlpha, breiteAlpha*10**3))
print("Auflösevermögen Beta: ", h(EnergieBeta, breiteBeta*10**3))


print("-----------------")
print("K-Kante Brom: ",     "\t", "\t", thetaBr[8])
print("K-Kante Gallium: ","\t", thetaGa[9])
print("K-Kante Strontium: ", "\t", thetaSr[8])
print("K-Kante Zink: ", "\t", "\t", thetaZn[7])
print("K-Kante Zirkonium: ", "\t", thetaZr[-1])
print("-----------------")
print("Energie Brom: ", "\t", y(13.5)/1000)
print("Energie Gallium: ","\t", y(17.6)/1000)
print("Energie Strontium: ", "\t", y(11.3)/1000)
print("Energie Zink: ", "\t", "\t", y(18.8)/1000)
print("Energie Zirkonium: ", "\t", y(10.3)/1000)
print("-----------------")


print("Theo Brom: ",EnergieBrom)
print("Theo Gallium: ",EnergieGallium)
print("Theo Strontium: ",EnergieStrontium)
print("Theo Zink: ",EnergieZink)
print("Theo Zirkonium: ",EnergieZirkonium)
print("-----------------")

print("Abweichung Energie Brom: ", (y(13.5)-EnergieBrom)/EnergieBrom *100)
print("Abweichung Energie Gallium: ","\t", (y(17.6)-EnergieGallium)/EnergieGallium *100)
print("Abweichung Energie Strontium: ", "\t", (y(11.3)-EnergieStrontium)/EnergieStrontium *100)
print("Abweichung Energie Zink: ", "\t", "\t", (y(18.8)-EnergieZink)/EnergieZink *100)
print("Abweichung Energie Zirkonium: ", "\t", (y(10.3)-EnergieZirkonium)/EnergieZirkonium *100)
print("-----------------")
alpha = 7.297e-3


def abschirmkonsti(E_K, Z): 
    w = np.sqrt((E_K / Ryd) - (alpha**2 * Z**4 / 4))
    return (Z - w)



AbschirmBrom = abschirmkonsti(EnergieBrom, 35)
AbschirmGallium = abschirmkonsti(EnergieGallium, 31)
AbschirmStrontium = abschirmkonsti(EnergieStrontium, 38)
AbschirmZink = abschirmkonsti(EnergieZink,30)
AbschirmZirkonium = abschirmkonsti(EnergieZirkonium,40)

AbschirmBromTheo = 3.55
AbschirmGalliumTheo = 3.41
AbschirmStrontiumTheo = 3.61
AbschirmZinkTheo = 3.37
AbschirmZirkoniumTheo = 3.65

print("Abschirmkonstante Brom: ", AbschirmBrom)
print("Abschirmkonstante Gallium: ", AbschirmGallium)
print("Abschirmkonstante Strontium: ", AbschirmStrontium)
print("Abschirmkonstante Zink: ", AbschirmZink)
print("Abschirmkonstante Zirkonium: ", AbschirmZirkonium)
print("-----------------")
print("Abweichung Abschirm Brom: ", (AbschirmBrom-AbschirmBromTheo)/AbschirmBromTheo*100)
print("Abweichung Abschirm Gallium: ", (AbschirmGallium-AbschirmGalliumTheo)/AbschirmGalliumTheo*100)
print("Abweichung Abschirm Strontium: ", (AbschirmStrontium-AbschirmStrontiumTheo)/AbschirmStrontiumTheo*100)
print("Abweichung Abschirm Zink: ", (AbschirmZink-AbschirmZinkTheo)/AbschirmZinkTheo*100)
print("Abweichung Abschirm Zirkonium: ", (AbschirmZirkonium-AbschirmZirkoniumTheo)/AbschirmZirkoniumTheo*100)

#Tabellen für Latex erzeugen:
print("-----------------")

# n = len(theta)
# for i in range(n):
#     print(theta[i], " & ", Rate[i], " ;")
#     i += 1


# n = len(thetaBr)
# for i in range(n):
#     print(thetaBr[i], " & ", RateBr[i], " ;")
#     i += 1

# n = len(thetaGa)
# for i in range(n):
#     print(thetaGa[i], " & ", RateGa[i], " ;")
#     i += 1

# n = len(thetaSr)
# for i in range(n):
#     print(thetaSr[i], " & ", RateSr[i], " ;")
#     i += 1

# n = len(thetaZn)
# for i in range(n):
#     print(thetaZn[i], " & ", RateZn[i], " ;")
#     i += 1

# n = len(thetaZr)
# for i in range(n):
#     print(thetaZr[i], " & ", RateZr[i], " ;")
#     i += 1
"""