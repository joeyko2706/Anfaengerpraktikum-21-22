import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

#f, A1, A2, a, b = np.genfromtxt('../Dateien/Aufgabebc.txt', unpack = True)
data = np.genfromtxt('../Dateien/Aufgabebc.txt', delimiter=';', names=True)
#print(data['f'])
#print(data['A1'])
#print(data['A2'])
#print(data['a'])
#print(data['b'])

plt.plot(data['f'], data['A1'], label = r'Amplitude $A_1 \:/\:$ V')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Messwert')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
plt.clf()

plt.plot(data['f'], data['A2'], label = r'Amplitude $A_2 \:/\:$ V')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Messwert')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.clf()

plt.plot(data['f'], data['a'], label = r'$a \:/\:$ ms')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Messwert')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')
plt.clf()

plt.plot(data['f'], data['b'], label = r'$b \:/\:$ ms')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Messwert')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot4.pdf')
plt.clf()
