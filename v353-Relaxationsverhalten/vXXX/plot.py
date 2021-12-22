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

daten = np.genfromtxt('../Dateien/Aufgabea.txt', delimiter=';', names=True)
#print(daten['U'])
#print(daten['t'])

plt.plot(daten['U'], daten['t'], 'r.')
plt.xlabel(r'$ U \:/\:$ V')
plt.ylabel(r'$t \:/\:$ ms')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plota.pdf')
plt.clf()


data = np.genfromtxt('../Dateien/Aufgabebc.txt', delimiter=';', names=True)
#print(data['f'])
#print(data['A1'])
#print(data['A2'])
#print(data['a'])
#print(data['b'])

plt.plot(data['f'], data['A1'], 'r.', label = r'Amplitude $A_1 \:/\:$ V')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Amplitude $A_1 \:/\:$ V')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotbc1.pdf')
plt.clf()

plt.plot(data['f'], data['A2'], 'r.', label = r'Amplitude $A_2 \:/\:$ V')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Amplitude $A_2 \:/\:$ V')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotbc2.pdf')
plt.clf()

plt.plot(data['f'], data['a'], 'r.', label = r'$a \:/\:$ ms')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$a \:/\:$ ms')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotbc3.pdf')
plt.clf()

plt.plot(data['f'], data['b'], 'r.', label = r'$b \:/\:$ ms')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$b \:/\:$ ms')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotbc4.pdf')
plt.clf()
