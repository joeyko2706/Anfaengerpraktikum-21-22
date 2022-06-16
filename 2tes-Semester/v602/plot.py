import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
from uncertainties import ufloat

# Konstanten definieren

c = const.c
h = const.h
d = 201.4 * 10**(-12) 
e = const.e

# Daten ziehen

theta, Rate = np.genfromtxt("data/Roentgenemission/emission", unpack = True)
thetaBr, RateBr = np.genfromtxt("data/Roentgenemission/brom", unpack = True)
thetaGa, RateGa = np.genfromtxt("data/Roentgenemission/gallium_richtig", unpack = True)
thetaSr, RateSr = np.genfromtxt("data/Roentgenemission/strontium", unpack = True)
thetaZn, RateZn = np.genfromtxt("data/Roentgenemission/zink", unpack = True)
thetaZr, RateZr = np.genfromtxt("data/Roentgenemission/Zirkonium", unpack = True)


# Vorbereitungsaufgabe


def f(E): #Funktion, um die Energien in der Vorbereitungsaufgabe zu bestimmen
    a = np.arcsin((h*c)/(2 * d * E * e))
    return np.rad2deg(a)


# print("Winkel Germanium:", f(11114)) #bereits in eV
# print("Winkel Brom:", f(13484))
# print("Winkel Rubidium :", f(15208))
# print("Winkel Strontium :", f(16115))
# print("Winkel Zirconium:", f(18008))
# print("Winkel Gallium:", f(10368))

#Emissionsspektrum

def l(theta):
    return 2*d*np.sin(theta*np.pi/180)

def E(theta):
    return (h*c)/(l(theta)*e)


def g(theta): #Funktion, um die Energien durch den Winkel zu bestimmen
    theta = np.rad2deg(theta)
    return (h*c)/(2 * d * np.sin((theta) *e))


def h(Energie,Breite):  #Funktion, um das Auflösevermögen zu bestimmen
    return (Energie/Breite)


def schoenerPlot():
    plt.legend()
    plt.xlabel(r"$2\vartheta$ / DEG")
    plt.ylabel(r"Zählrate")
    plt.tight_layout(pad=0, h_pad=1.09, w_pad=1.09)
    plt.grid()


alphaMax = Rate[175]    #Peak von Alpha
betaMax = Rate[152]      #Peak von Beta
breiteAlpha = np.round(20.451 - 20.0, 3)    #Halbwertsbreite von der K-Alpha Linie
breiteBeta = np.round(22.71 - 22.29, 3)     #von beta

print("Maximum Beta: ", theta[152], betaMax, "Halbwertsbreite (y): ", 1/2 * betaMax, "Breite (x): ", breiteBeta)
print("Maximum Alpha: ", theta[175], alphaMax, "Halbwertsbreite (y): ", 1/2 * alphaMax, "Breite (x): ", breiteAlpha)

EnergieAlpha = 8047.823 # Energien der beiden Absorptionskanten in eV
EnergieBeta = 8905.413
EnergieAlphaGemessen = E(22.5) #Die Funktion funktioniert irgendwie nicht mehr, deswegen manuell implementieren
EnergieBetaGemessen = E(20.2)

EnergieAlphaGemessen = 8043.355
EnergieBetaGemessen = 8914.204


print("Energie Alpha: ", EnergieAlphaGemessen)
print("Energie Beta: ", EnergieBetaGemessen)
print("Abweichung von Alpha: ", (EnergieAlphaGemessen-EnergieAlpha)/EnergieAlpha * 100, "%")
print("Abweichung von Beta: ", (EnergieBetaGemessen-EnergieBeta)/EnergieBeta * 100, "%")
print("Auflösevermögen Alpha: ", h(EnergieAlpha,breiteAlpha))
print("Auflösevermögen Beta: ", h(EnergieBeta,breiteBeta))


#Plots programmieren
# print("Plot 1")


plt.plot(theta, Rate, "b", alpha=0.7)
plt.plot(theta, Rate, "r.", label="Messwerte", markersize=5, markeredgewidth=0.5, markeredgecolor="k")
plt.plot(theta[175], Rate[175], ".", color="limegreen", label=r"$K_\alpha$-Kante")
plt.plot(theta[152], Rate[152], ".", color="magenta", label=r"$K_\beta$-Kante")
# plt.plot(theta[77], Rate[77], ".", color="dodgerblue", label="Bremsberg")
schoenerPlot()
plt.savefig('build/plot1.pdf')
plt.clf()



plt.plot(theta[140:185], Rate[140:185], "b", alpha=0.7)
plt.plot(theta[140:185], Rate[140:185], "r.", label="Messwerte", markersize=5, markeredgewidth=0.5, markeredgecolor="k")
plt.plot(theta[175], Rate[175],  ".", color="limegreen", label=r"$K_\alpha$-Kante")
plt.plot(theta[152], Rate[152], ".", color="magenta", label=r"$K_\beta$-Kante")

plt.hlines(702.0, 20, 20.451, linewidth=1, color="magenta") #beta
plt.hlines(2540.0, 22.29, 22.71, linewidth=1, color="limegreen")    #alpha

schoenerPlot()
plt.savefig('build/plot2.pdf')
plt.clf()


#Absorbtionsspektren programmieren



#Brom

plt.plot(thetaBr, RateBr, "b", alpha=0.5)
plt.plot(thetaBr, RateBr, "r.", label="Messwerte des Bromabsorbers")
# plt.vlines(thetaBr[8], RateBr[0], RateBr[8], color="limegreen", label=r"K-Kante")
plt.axvline(thetaBr[8], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig('build/plot3.pdf')
plt.clf()

#Gallium

plt.plot(thetaGa, RateGa, "b", alpha=0.5)
plt.plot(thetaGa, RateGa, "r.", label="Messwerte des Galliumabsorbers")
# plt.vlines(thetaGa[6], RateGa[0], RateGa[6], color="limegreen", label=r"K-Kante")
plt.axvline(thetaGa[6], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig('build/plot4.pdf')
plt.clf()

# Strontium

plt.plot(thetaSr, RateSr, "b", alpha=0.5)
plt.plot(thetaSr, RateSr, "r.", label="Messwerte des Strontiumabsorbers")
# plt.vlines(thetaSr[6], RateSr[0], RateSr[6], color="limegreen", label=r"K-Kante")
plt.axvline(thetaSr[6], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig('build/plot5.pdf')
plt.clf()

# Zink

plt.plot(thetaZn, RateZn, "b", alpha=0.5)
plt.plot(thetaZn, RateZn, "r.", label="Messwerte des Zinkabsorbers")
# plt.vlines(thetaZn[5], RateZn[0], RateZn[5], color="limegreen", label=r"K-Kante")
plt.axvline(thetaZn[5], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig('build/plot6.pdf')
plt.clf()

# Zirkonium

plt.plot(thetaZr, RateZr, "b", alpha=0.5)
plt.plot(thetaZr, RateZr, "r.", label="Messwerte des Zirkoniumabsorbers")
# plt.vlines(thetaZr[5], RateZr[0], RateZr[5], color="limegreen", label=r"K-Kante")
plt.axvline(thetaZr[5], color="limegreen", label=r"K-Kante")
schoenerPlot()
plt.savefig('build/plot7.pdf')
plt.clf()


# Berechnungen