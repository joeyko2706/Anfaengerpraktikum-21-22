import numpy as np
import scipy.constants as const
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


laufzeiten = np.array([4.0, 4.9, 4.8, 3.2])
amplituden = np.array([1.30, 1.30, 1.25 ,0.80])
perioden = np.array([0.50, 0.54, 0.58, 0.54, 0.57])

mittelLaufz= ufloat(np.mean(laufzeiten), np.std(laufzeiten))
mittelAmplit= ufloat(np.mean(amplituden), np.std(amplituden))
mittelPeriod = ufloat(np.mean(perioden), np.std(perioden))


print("Mittelwert Laufzeiten: ", mittelLaufz)
print("Mittelwert Amplituden: ", mittelAmplit)
print("Mittelwert Periodenlänge: ", mittelPeriod)

ZylinderLaufzeiten = np.array([18.32, 34.43, 43.96, 79.12])


def schallgeschwindigkeit(s, t):
    return ((2*s*10**(-3))/(t*10**(-6)))


# Schallgeschwindigkeiten mit dem Impuls-Echo-Verfahren

print("Schallgeschwindigkeiten: ") # Durch zwei, wegen Impuls echo
schalli1 = schallgeschwindigkeit(40.4, 18.32)/2
schalli2 = schallgeschwindigkeit(61.5, 34.43)/2
schalli3 = schallgeschwindigkeit(80.5, 43.96)/2
schalli4 = schallgeschwindigkeit(120.5, 79.12)/2

print("Schallgeschwindigkeit 1 = ", schalli1)
print("Schallgeschwindigkeit 2 = ", schalli2)
print("Schallgeschwindigkeit 3 = ", schalli3)
print("Schallgeschwindigkeit 4 = ", schalli4)

schallZylinder1 = np.ones(4)

schallZylinder1[0] *= schalli1
schallZylinder1[1] *= schalli2
schallZylinder1[2] *= schalli3
schallZylinder1[3] *= schalli4

mittelWertSchallZyl1 = ufloat(np.mean(schallZylinder1), np.std(schallZylinder1))
print("Mittelwert Schallgeschwindigkeit Zylnder: ", mittelWertSchallZyl1)


# Schallgeschwindigkeiten mit dem Durchschallungsverfahren. Natürlich dieselbe Vorgehensweise

schalli1 = schallgeschwindigkeit(40.4, 30.04)
schalli2 = schallgeschwindigkeit(61.5, 43.96)
schalli3 = schallgeschwindigkeit(80.5, 59.34)
schalli4 = schallgeschwindigkeit(120.5, 88.28)

print("Schallgeschwindigkeit 1 = ", schalli1)
print("Schallgeschwindigkeit 2 = ", schalli2)
print("Schallgeschwindigkeit 3 = ", schalli3)
print("Schallgeschwindigkeit 4 = ", schalli4)

schallZylinder2 = np.ones(4)

schallZylinder2[0] *= schalli1
schallZylinder2[1] *= schalli2
schallZylinder2[2] *= schalli3
schallZylinder2[3] *= schalli4

mittelWertSchallZyl2 = ufloat(np.mean(schallZylinder2), np.std(schallZylinder2))
print("Mittelwert Schallgeschwindigkeit Zylnder: ", mittelWertSchallZyl2)

#   Amplituden berechen
"""
Um die Amplitude zu berechnen, müssen alle Werte mit e^(Q/10) multipliziert werden, wobei Q
die Verstärkung ist. Die Rechnungen sind ebendiese Rechnungen.
Die Zahl hinter der Variable ist immer die Kennzeichnung des Zylinders!
"""

Amplitude2 = 0.48 * np.exp(14.8/10)
Amplitude3 = 1.22 * np.exp(28.75/10)
Amplitude4 = 0.21 * np.exp(28.75/10)

np.round(Amplitude2, 3)
np.round(Amplitude3, 3)
np.round(Amplitude4, 3)

print("Amplitude 2: ",Amplitude2)
print("Amplitude 3: ",Amplitude3)
print("Amplitude 4: ",Amplitude4)
