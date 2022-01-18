import matplotlib.pyplot as plt
import numpy as np


T = np.array([296, 299, 302, 305, 308, 311, 314, 317, 320, 323])
eta = np.array([436, 417, 386, 365, 344, 327, 307, 294, 278, 263])
x = 1/T
y = np.log(eta/10000)

# Lineare Regression
params, covariance_matrix = np.polyfit(x, y, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x_plot = np.linspace(0.00309, 0.00342, 100000)
plt.plot(x, y, 'x', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=1,
)
plt.grid()
plt.xlabel(r'$\frac{1}{T}\,/\,K$')
plt.ylabel(r'$ln\left(\frac{\eta}{Pa}\cdot s\right)$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')