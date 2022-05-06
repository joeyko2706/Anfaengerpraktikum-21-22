import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat


alpha, I = np.genfromtxt(
    "data/aufgabe1pPol.txt", unpack=True
)  # Die Daten für parallele Polarisation Importieren.
alpha1, I1 = np.genfromtxt(
    "data/aufgabe1sPol.txt", unpack=True
)  # Die Daten für senkrechte Polarisation Importieren.
n = alpha.size

I_e = 0.54 * 10 ** (-3)  # Nullstrom in A
E_e = np.sqrt(I_e)
alphaBogen = alpha / 180 * np.pi  # Winkel in Bogenmaß umrechnen
y1 = np.sqrt(I * 10 ** (-4) / I_e)
y2 = np.sqrt(I1 * 10 ** (-4) / I_e)


def pPolarisation(
    w, I
):  # Brechungsindex für pPolarisiertes Licht; w = winkel, I = Photostrom
    E = E_e / np.sqrt(I * 10 ** (-6))
    return (
        (1 + E)
        / (np.cos(w) * (1 - E))
        * np.sqrt(1 / 2 * (1 + (np.sqrt(2 * w)) ** 2 * ((1 - E) ** 2 / (1 + E) ** 2)))
    )


def sPolarisation(
    w, I
):  # Brechungsindex für sPolarisiertes Licht; w = winkel, I = photostrom
    E = E_e / np.sqrt(I * 10 ** (-6))
    return np.sqrt(1 + (4 * E * (np.cos(w)) ** 2) / (E - 1) ** 2)


def pPolTheorie(n, a, E):
    return (
        ((np.sqrt(n ** 2 - (np.sin(np.deg2rad(a))) ** 2) - np.cos(np.deg2rad(a))) ** 2)
        / (n ** 2 - 1)
    ) - E


def sPolTheorie(n, a, E):
    return (
        (
            (n ** 2) * np.cos(np.deg2rad(a))
            - np.sqrt((n ** 2) - (np.sin(np.deg2rad(a)) ** 2))
        )
        / (
            (n ** 2) * np.cos(np.deg2rad(a))
            + np.sqrt((n ** 2) - (np.sin(np.deg2rad(a)) ** 2))
        )
    ) - E


pBrechung = np.round(pPolarisation(alpha, I), 3)
sBrechung = np.round(sPolarisation(alpha1, I1), 3)
winkeltheo = np.linspace(10, 88, 1000)

# Die folgenden 6 Zeilen sind nur Befehle, um die Mittelwerte und die Tabellen auszugeben

# print("Mittelwert Brechung bei sPol: ", np.round(np.mean(sBrechung),4), "+/-" , np.round(np.std(sBrechung))) #Mittelwert des Brechungsindex bei sPolarisiertem Licht
# print("Mittelwert Brechung bei pPol: ", np.round(np.mean(pBrechung),4), "+/-" , np.round(np.std(pBrechung))) #Mittelwert des Brechungsindex bei pPolarisiertem Licht
# for i in range(n):
#     print(alpha[i]," & ", I[i]," & ", pBrechung[i]," ;")    #Tabelle für parallele Polarisation
#     print(alpha1[i]," & ", I1[i]," & ", sBrechung[i]," ;")  #Tabelle für senkrechte Polarisation
#     i += 1


plt.plot(alpha, y1, ".", label="Messwerte $\qty{90}{\degree}$$")  # pPol
plt.plot(
    winkeltheo,
    pPolTheorie(3.35268, winkeltheo, 0),
    label="Theoriekurve $\qty{90}{\degree}$",
)
plt.xlabel(r"Winkel $\alpha$ / Grad")
plt.ylabel(r"$\sqrt{\frac{I_r}{I_e}}$")

plt.plot(alpha1, y2, ".", label="Messwerte $\qty{0}{\degree}$")  # sPol
plt.plot(
    winkeltheo,
    abs(sPolTheorie(3.35268, winkeltheo, 0)),
    label="Theoriekurve $\qty{0}{\degree}$",
)
plt.xlabel(r"Winkel $\alpha$ / Grad")
plt.ylabel(r"$\sqrt{\frac{I_r}{I_e}}$")

plt.grid()
plt.legend()
plt.savefig("build/plot1.pdf")
