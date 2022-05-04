import matplotlib.pyplot as plt
import numpy as np


alpha, I = np.genfromtxt("data/aufgabe1pPol.txt", unpack=True)

plt.plot(alpha, I, "r", label="Messwerte")
plt.plot(alpha, I, ".", label="Messwerte")
plt.xlabel(r"Winkel")
plt.ylabel(r"Strom")
plt.legend()
plt.grid()
plt.close()

alpha1, I1 = np.genfromtxt("data/aufgabe1sPol.txt", unpack=True)

plt.plot(alpha1, I1, "r", label="Messwerte")
plt.plot(alpha1, I1, ".", label="Messwerte")
plt.xlabel(r"Winkel")
plt.ylabel(r"Strom")
plt.legend()
plt.grid()
plt.close()
