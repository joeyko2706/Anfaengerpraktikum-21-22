import numpy as np

# Konstanten definieren:

rho_doppler = 1.15  # g/cm^3
c_L = 1800  # m/s
visko_doppler = 12  # mPa s
c_p = 2700  # m/s
l = 30.7  # mm


# Dopplerwinkel berechnen


doppler15 = 80.0641
doppler30 = 70.5288
doppler45 = 61.8745

print("Dopplerwinkel 15°: ", doppler15)
print("Dopplerwinkel 30°: ", doppler30)
print("Dopplerwinkel 45°: ", doppler45)

# Strömungsgeschwindigkeiten berechnen


def stroemi(
    diff, x
):  # Funktion, um die Strömungsgeschwindigkeit zu berechnen. diff ist die Frequenzdifferenz, die gesendete Frequenz ist 2MHz und x der Winkel
    v = (c_L * diff) / (2 * 2 * 10 ** 6 * np.cos(x))
    return v


print(
    "Stroemi unter 15°: ",
    np.round(stroemi(45, doppler15), 4),
    np.round(stroemi(62, doppler15), 4),
    np.round(stroemi(91, doppler15), 4),
    np.round(stroemi(175, doppler15), 4),
    np.round(stroemi(186, doppler15), 4),
)
print(
    "Stroemi unter 30°: ",
    np.round(stroemi(55, doppler30), 4),
    np.round(stroemi(102, doppler30), 4),
    np.round(stroemi(152, doppler30), 4),
    np.round(stroemi(1246, doppler30), 4),
    np.round(stroemi(355, doppler30), 4),
)
print(
    "Stroemi unter 45°: ",
    np.round(stroemi(96, doppler45), 4),
    np.round(stroemi(184, doppler45), 4),
    np.round(stroemi(298, doppler45), 4),
    np.round(stroemi(461, doppler45), 4),
    np.round(stroemi(643, doppler45), 4),
)
