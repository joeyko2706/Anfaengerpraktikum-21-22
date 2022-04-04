import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

x = np.array([9.99, 8.00, 6.47, 5.02, 4.00, 3.00, 2.03]) #Kopplungskapazität in nF +- 0.3%
y = np.array([13, 11, 10, 8, 7, 6, 4])

plt.plot(x, y, 'r.', label = 'Messwerte')
plt.xlabel(r'Kopplungskapazität')
plt.ylabel(r'Schwingungsmaxima')
plt.legend()
plt.savefig('test.pdf')


#Ich glaube, dass wir diese Plots garnicht brauchen!!!