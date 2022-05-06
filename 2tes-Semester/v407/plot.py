import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat


alpha, I = np.genfromtxt("data/aufgabe1pPol.txt", unpack=True)  #Die Daten für parallele Polarisation Importieren.
alpha1, I1 = np.genfromtxt("data/aufgabe1sPol.txt", unpack=True)#Die Daten für senkrechte Polarisation Importieren.
n = alpha.size

I_e = 0.54*10**(-3)             #Nullstrom in A
E_e = np.sqrt(I_e)  
alphaBogen = alpha/180 * np.pi  #Winkel in Bogenmaß umrechnen


def pPolarisation(w, I):#Brechungsindex für pPolarisiertes Licht; w = winkel, I = Photostrom
    E = E_e / np.sqrt(I*10**(-6))
    return (1+E)/(np.cos(w) * (1 - E)) * np.sqrt(1/2 * (1 + (np.sqrt(2 * w))**2 * ((1-E) **2 / (1+E) **2) ))


def sPolarisation(w, I):#Brechungsindex für sPolarisiertes Licht; w = winkel, I = photostrom
    E = E_e / np.sqrt(I*10**(-6))
    return np.sqrt(1 + (4 * E * (np.cos(w))**2) / (E-1)**2 )


pBrechung = np.round(pPolarisation(alpha, I), 3)
sBrechung = np.round(sPolarisation(alpha1, I1), 3)


for i in range(n):
    # print(alpha[i]," & ", I[i]," & ", pBrechung[i]," ;")    #Tabelle für parallele Polarisation
    print(alpha1[i]," & ", I1[i]," & ", sBrechung[i]," ;")  #Tabelle für senkrechte Polarisation
    i += 1


# print("Mittelwert Brechung bei sPol: ", np.round(np.mean(sBrechung),4), "+/-" , np.round(np.std(sBrechung))) #Mittelwert des Brechungsindex bei sPolarisiertem Licht
# print("Mittelwert Brechung bei pPol: ", np.round(np.mean(pBrechung),4), "+/-" , np.round(np.std(pBrechung))) #Mittelwert des Brechungsindex bei pPolarisiertem Licht

plt.plot(alpha, pBrechung, ".", label = "Messwerte")
plt.xlabel(r"Winkel $\alpha \mathbin{/} \unit{\degree}$")
plt.ylabel(r"Brechungsindex $n$")
plt.grid()
plt.legend()
plt.title("Brechungsindex bei paralleler Polarisation")
# plt.show()
plt.savefig("build/plot1.pdf")
