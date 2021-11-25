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

#Frequenzen müssen noch mit Kästchen multipliziert werden
# selbiges gilt für die Spannungen

f_1 = np.array([2.1, 2.2, 2.2, 2.1, 2.2, 2.2, 2.2, 2.2])
f_2 = np.array([2.7, 2.7, 2.8, 3.0, 3.2, 3.4, 4.0, 4.2])
x = np.array([9.99, 8.00, 6.47, 5.02, 4.00, 3.00, 2.03, 1.01]) #Kopplungskapazität in nF +- 0.3%
v_1 = np.array([1.2, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1])
v_2 = np.array([2.2, 2.2, 2.2, 2.2, 2.1, 2.1, 2.0, 1.9])

dreisatz1 = f_1 * 100 / 30
dreisatz2 = f_2 * 100 / 30



plt.plot(x , dreisatz1 , 'b.', label = 'Frequenz')
plt.plot(x, v_1, 'r.', label = 'Spannung')
plt.legend()
plt.xlabel(r'$C_K /$ nF')
plt.ylabel(r'$f_{1,\text{max}}, $V / mV')
plt.savefig('build/freq1.pdf')


plt.clf()

plt.plot(x, dreisatz2 , 'b.', label = 'Frequenz')
plt.plot(x, v_2 , 'r.', label = 'Spannung')
plt.legend()
plt.xlabel(r'$C_K /$ nF')
plt.ylabel(r'$f_{2,\text{max}}, V /$ mV')
plt.savefig('build/freq2.pdf')


#Ich bin mir über die Einheit der y-Achse noch nicht ganz sicher.