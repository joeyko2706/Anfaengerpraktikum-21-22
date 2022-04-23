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
    diff, fmean, x
):  # Funktion, um die Strömungsgeschwindigkeit zu berechnen. diff ist die Frequenzdifferenz, fmean die gesendete Frequenz und x der Winkel
    v = (c_L * diff) / (2 * fmean * np.cos(x))
    return v


print(
    "Stroemi unter 15°: ",
    np.round(stroemi(45, 49, doppler15), 4),
    np.round(stroemi(62, 73, doppler15), 4),
    np.round(stroemi(91, 110, doppler15), 4),
    np.round(stroemi(175, 208, doppler15), 4),
    np.round(stroemi(186, 208, doppler15), 4),
)
print(
    "Stroemi unter 30°: ",
    np.round(stroemi(55, 73, doppler30), 4),
    np.round(stroemi(102, 122, doppler30), 4),
    np.round(stroemi(152, 183, doppler30), 4),
    np.round(stroemi(1246, 287, doppler30), 4),
    np.round(stroemi(355, 409, doppler30), 4),
)
print(
    "Stroemi unter 45°: ",
    np.round(stroemi(96, 122, doppler45), 4),
    np.round(stroemi(184, 244, doppler45), 4),
    np.round(stroemi(298, 391, doppler45), 4),
    np.round(stroemi(461, 659, doppler45), 4),
    np.round(stroemi(643, 897, doppler45), 4),
)
print(
    "Stroemi unter 45°, die zweite: ",
    np.round(stroemi(96, 218, doppler45), 4),
    np.round(stroemi(184, 428, doppler45), 4),
    np.round(stroemi(298, 689, doppler45), 4),
    np.round(stroemi(461, 1120, doppler45), 4),
    np.round(stroemi(643, 1540, doppler45), 4),
)