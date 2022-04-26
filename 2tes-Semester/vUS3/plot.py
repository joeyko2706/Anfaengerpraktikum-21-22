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


plt.plot(
    v_fluss15,
    nu15 / np.cos(alpha[0]),
    color="b",
    marker="x",
    linewidth=0,
    label=r"$\varphi = \qty{15}{\degree}$",
)
plt.plot(
    v_fluss30,
    nu30 / np.cos(alpha[1]),
    color="darkmagenta",
    marker="+",
    linewidth=0,
    label=r"$\varphi = \qty{30}{\degree}$",
)
plt.plot(
    v_fluss45,
    nu45 / np.cos(alpha[2]),
    color="crimson",
    marker=".",
    linewidth=0,
    label=r"$\varphi = \qty{45}{\degree}$",
)
plt.xlabel(r"$v_\text{Fluss} \,/\, \si{\metre\per\second}$")
plt.ylabel(r"$\upDelta \nu\,/\, \si{\hertz}$")
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig("build/plot.pdf")
plt.close()
print("Plot 1/3")

# Messaufgabe 2)

# t, I, v = np.genfromtxt('data/Aufgabeb45per.txt', unpack = True)


# def p2(x,a,b,c):    #Fit: Polynom 2ten Grades
#     return a*x**2 + b*x + c

# Erster Plot links

# params, pcov = op.curve_fit(p2, t, I)
# x = np.linspace(13,17.5,1000)
# plt.subplot(1,2,1)
# plt.plot(t, I, marker = 'x' ,color = 'crimson', linewidth = 0, label = 'Messwerte')
# plt.plot(x, p2(x, *params), color = 'mediumblue', label = 'Fit')

# plt.grid()
# plt.legend(loc='best')
# plt.xlabel(r'Messtiefe in $\unit{\micro\second}$')
# plt.ylabel(r'$I \mathbin{/} \unit{\kilo\volt\squared\per\second}$')
# plt.title('Signalintensität')
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

# Zweiter Plot rechts

# params, pcov = op.curve_fit(p2, t, v)
# plt.subplot(1,2,2)
# plt.plot(t, v, marker = 'x' ,color = 'firebrick', linewidth = 0)
# plt.plot(x, p2(x, *params), color = 'cornflowerblue', label = 'Fit')


# plt.xlabel(r'Messtiefe in $\unit{\micro\second}$')
# plt.ylabel(r'$v \mathbin{/} \unit{\centi\metre\per\second}$')
# plt.grid()
# plt.title('momentane Fließgeschwindigkeit')
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot2_1.pdf')
# plt.close()
# print('Plot 2/3')
