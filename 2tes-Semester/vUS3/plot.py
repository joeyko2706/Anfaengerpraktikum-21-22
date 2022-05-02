import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as op

print("Plots werden durchgegangen")

c_L = 1800
c_P = 2700
nu_0 = 2 * 10 ** 6
theta = [np.pi / 12, np.pi / 6, np.pi / 4]
alpha = (np.pi / 2) - np.arcsin(np.sin(theta) * (c_L / c_P))

# Messaufgabe 1)

nu15 = np.array([45, 62, 91, 175, 186])
nu30 = np.array([55, 102, 152, 246, 355])
nu45 = np.array([96, 184, 298, 461, 643])

doppler15 = 80.0641
doppler30 = 70.5288
doppler45 = 61.8745

v_fluss15 = nu15 * c_L / (2 * nu_0 * np.cos(alpha[0]))
v_fluss30 = nu30 * c_L / (2 * nu_0 * np.cos(alpha[1]))
v_fluss45 = nu45 * c_L / (2 * nu_0 * np.cos(alpha[2]))



y1 = nu15 / np.cos(alpha[0])
y2 = nu30 / np.cos(alpha[1])
y3 = nu45 / np.cos(alpha[2])


print('Stroumungsgeschwindigkeiten 15 Grad: ', np.round(v_fluss15,4) )
print('Stroumungsgeschwindigkeiten 30 Grad: ', np.round(v_fluss30,4))
print('Stroumungsgeschwindigkeiten 45 Grad: ', np.round(v_fluss45,4))


x1 = np.linspace(0, 0.5, 10)
x2 = np.linspace(0, 0.5, 10)
x3 = np.linspace(0, 0.65, 10)


def p1(x, a, b):  # Fit: Polynom 1ten Grades
    return a * x + b


params1, pcov1 = op.curve_fit(p1, v_fluss15, y1)


# Plot für 15 Grad


plt.plot(
    v_fluss15,
    y1,
    color="r",
    marker=".",
    linewidth=0,
    label=r"$\varphi = \qty{15}{\degree}$",
)
plt.plot(x1, p1(x1, *params1), color="b", label="Fit")
plt.xlabel(r"$v_\text{Fluss} \,/\, \si{\metre\per\second}$")
plt.ylabel(r"$\upDelta \nu\,/\, \si{\hertz}$")
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/plota.pdf')
plt.close()
print("Plot 1/5")

# Plot für 30 Grad


params2, pcov2 = op.curve_fit(p1, v_fluss30, y2)
plt.plot(
    v_fluss30,
    y2,
    color="r",
    marker=".",
    linewidth=0,
    label=r"$\varphi = \qty{30}{\degree}$",
)
plt.plot(x2, p1(x2, *params2), color="b", label="Fit")
plt.xlabel(r"$v_\text{Fluss} \,/\, \si{\metre\per\second}$")
plt.ylabel(r"$\upDelta \nu\,/\, \si{\hertz}$")
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/plotb.pdf')
print("Plot 2/5")
plt.close()


# Plot für 45 Grad

params3, pcov3 = op.curve_fit(p1, v_fluss45, y3)
plt.plot(
    v_fluss45,
    y3,
    color="r",
    marker=".",
    linewidth=0,
    label=r"$\varphi = \qty{45}{\degree}$",
)
plt.plot(x3, p1(x3, *params3), color="b", label="Fit")


plt.xlabel(r"$v_\text{Fluss} \,/\, \si{\metre\per\second}$")
plt.ylabel(r"$\upDelta \nu\,/\, \si{\hertz}$")
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig("build/plotc.pdf")
plt.close()
print("Plot 3/5")

# Messaufgabe 2)

t, I, v = np.genfromtxt("data/Aufgabeb45per.txt", unpack=True)


def p2(x, a, b, c):  # Fit: Polynom 2ten Grades
    return a * x ** 2 + b * x + c


# 45Prozent
# Erster Plot links

params4, pcov4 = op.curve_fit(p2, t, I)
x = np.linspace(13, 17.5, 1000)
plt.subplot(1, 2, 1)
plt.plot(t, I, marker="x", color="r", linewidth=0, label="Messwerte")
plt.plot(x, p2(x, *params4), color="b", label="Fit")

plt.grid()
plt.legend(loc="best")
plt.xlabel(r"Messtiefe in $\unit{\micro\second}$")
plt.ylabel(r"$I \mathbin{/} \unit{\kilo\volt\squared\per\second}$")
plt.title("Signalintensität")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

# Zweiter Plot rechts

params5, pcov5 = op.curve_fit(p2, t, v)
plt.subplot(1, 2, 2)
plt.plot(t, v, marker="x", color="r", linewidth=0)
plt.plot(x, p2(x, *params5), color="b", label="Fit")


plt.xlabel(r"Messtiefe in $\unit{\micro\second}$")
plt.ylabel(r"$v \mathbin{/} \unit{\centi\metre\per\second}$")
plt.grid()
plt.title("mom. Fließgeschwindigkeit")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/plot2.pdf")
plt.close()
print("Plot 4/5")

# 70Prozent
# Erster Plot links

t1, I1, v1 = np.genfromtxt("data/Aufgabeb70per.txt", unpack=True)


params, pcov = op.curve_fit(p2, t1, I1)
x1 = np.linspace(13, 17.5, 1000)
plt.subplot(1, 2, 1)
plt.plot(t1, I1, marker="x", color="r", linewidth=0, label="Messwerte")
plt.plot(x1, p2(x1, *params), color="b", label="Fit")

plt.grid()
plt.legend(loc="best")
plt.xlabel(r"Messtiefe in $\unit{\micro\second}$")
plt.ylabel(r"$I \mathbin{/} \unit{\kilo\volt\squared\per\second}$")
plt.title("Signalintensität")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

# Zweiter Plot rechts

params, pcov = op.curve_fit(p2, t1, v1)
plt.subplot(1, 2, 2)
plt.plot(t1, v1, marker="x", color="r", linewidth=0)
plt.plot(x1, p2(x, *params), color="b", label="Fit")


plt.xlabel(r"Messtiefe in $\unit{\micro\second}$")
plt.ylabel(r"$v \mathbin{/} \unit{\centi\metre\per\second}$")
plt.grid()
plt.title("mom. Fließgeschwindigkeit")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("build/plot3.pdf")
plt.close()
print("Plot 5/5")
