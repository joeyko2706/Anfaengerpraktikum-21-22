import numpy as np
from uncertainties import ufloat

x1 = ufloat(4.86, 0.15)
x2 = ufloat(14.16, 0.34)
x3 = ufloat(24.0, 0.5)
print((x1 + x2 + x3) / 3)
#Für das Gitter mit 100 Linien pro Millimeter ergibt sich $\lambda_\text{Rot} = (4,86 \pm 0,15) \cdot 10^9 \si{\meter}$ und
#$\lambda_\text{Grün} = (3,99 \pm 0,15) \cdot 10^9 \si{\meter}$.
#Für das Gitter mit 300 Linien pro Millimeter ergibt sich $\lambda_\text{Rot} = (1,416 \pm 0,034) \cdot 10^8 \si{\meter}$ und
#$\lambda_\text{Grün} = (1,165 \pm 0,15) \cdot 10^8 \si{\meter}$.
#Für das Gitter mit 600 Linien pro Millimeter ergibt sich $\lambda_\text{Rot} = (2,40 \pm 0,05) \cdot 10^8 \si{\meter}$ und
#$\lambda_\text{Grün} = (2,84 \pm 0,09) \cdot 10^8 \si{\meter}$.

# x1 = ufloat(np.sin(16.5 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x2 = ufloat(np.sin(29.5 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x3 = ufloat(np.sin(21 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x4 = ufloat(np.sin(9 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x5 = ufloat(np.sin(11.5 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x6 = ufloat(np.sin(14 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x7 = ufloat(np.sin(16 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))

# y1 = (0.1 *10**(-6) / 1) * x1
# y2 = (0.1 *10**(-6) / 2) * x2
# y3 = (0.1 *10**(-6) / 3) * x3
# y4 = (0.1 *10**(-6) / 4) * x4
# y5 = (0.1 *10**(-6) / 5) * x5
# y6 = (0.1 *10**(-6) / 6) * x6
# y7 = (0.1 *10**(-6) / 7) * x7

# print(y1)

# x1 = ufloat(38, 0.5)
# x2 = ufloat(38, 0.5)
# x3 = ufloat(38, 0.5)
# x4 = ufloat(40, 0.5)
# x5 = ufloat(43, 0.5)

# print((x1 + x2 + x3 + x4 + x5) / 5)
# # x = ufloat(1.48, 0.017)
# # print(2.9979 / x)

# x1 = ufloat(np.sin(38 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x2 = ufloat(np.sin(36 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x3 = ufloat(np.sin(31 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x4 = ufloat(np.sin(28.5 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x5 = ufloat(np.sin(26 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x6 = ufloat(np.sin(19.5 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x7 = ufloat(np.sin(13.5 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# x8 = ufloat(np.sin(7 * (np.pi / 180)), np.sin(0.5 * (np.pi / 180)))
# y1 = np.sin(70 * (np.pi / 180)) / x1
# y2 = np.sin(60 * (np.pi / 180)) / x2
# y3 = np.sin(50 * (np.pi / 180)) / x3
# y4 = np.sin(45 * (np.pi / 180)) / x4
# y5 = np.sin(40 * (np.pi / 180)) / x5
# y6 = np.sin(30 * (np.pi / 180)) / x6
# y7 = np.sin(20 * (np.pi / 180)) / x7
# y8 = np.sin(10 * (np.pi / 180)) / x8
# print((y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8) / 8)

# x = np.linspace(0, 10, 1000)
# y = x ** np.sin(x)

# plt.subplot(1, 2, 1)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
# plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
# plt.legend(loc='best')

# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
# plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
# plt.legend(loc='best')

# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot.pdf')
