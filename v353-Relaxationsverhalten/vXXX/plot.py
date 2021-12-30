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
#x1 = np.array([0.55, 0.50, 0.44, 0.40, 0.36, 0.32, 0.26, 0.24, 0.18, 0.12, 0.10, 0.04, -0.04, -0.06, -0.10, -0.14, -0.16, -0.18, -0.22, -0.24, -0.28, -0.30, -0.32, -0.34, -0.38, -0.40, -0.42, -0.44, -0.46, -0.48, -0.50])
#x = np.log(x1)
#y = np.array([0.00, 0.02, 0.04, 0.05, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48, 0.50, 0.52, 0.54, 0.56, 0.58, 0.60])

x1 = daten['U'] +2.5
x = np.log(x1)
y = daten['t']

N = len(y)
Delta = N * np.sum(x**2) - (np.sum(x))**2

A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta


#plt.plot(daten['U'], daten['t'], 'r.')
plt.plot(x, y, 'r.', label = 'Messwerte')
plt.plot(x, A*x + B, 'b', label='lineare Regression')
plt.legend()
plt.xlabel(r'$ U \:/\:$ V')
plt.ylabel(r'$t \:/\:$ ms')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plota.pdf')
plt.clf()


#Aufgabe b) und c)

data = np.genfromtxt('../Dateien/Aufgabebc.txt', delimiter=';', names=True)
#print(data['f'])
#print(data['A1'])
#print(data['A2'])
#print(data['a'])
#print(data['b'])



#Amplitude A1!

#plt.plot(data['f'], data['A1'], 'r.', label = r'Amplitude $A_1 \:/\:$ V')
#plt.xlabel(r'$f \:/\:$ kHz')
#plt.ylabel(r'Amplitude $A_1 \:/\:$ V')
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/plotbc1.pdf')
#plt.clf()


#Amplitude A2!

x2 = np.log(data['f'])
y = np.log(data['A2'])
N = len(data['A2'])
Delta = N * np.sum(data['f'] **2) - (np.sum(data['f']))**2

A1 = (N * np.sum(data['f'] * y) - np.sum(data['f']) * np.sum(y)) / Delta
B1 = (np.sum(data['f']**2) * np.sum(y) - np.sum(data['f']) * np.sum(data['f'] * y)) / Delta

plt.plot(data['f'], y, 'r.', label = 'Messwerte')
plt.plot(data['f'], A1*data['f'] + B1, 'b', label='lineare Regression')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'Amplitude $A_2 \:/\:$ V')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotbc2.pdf')
plt.clf()




phi = 360 * (data['a'] *10**(-3)) / (data['b'] *10**(-3))
N = len(phi)
Delta = N * np.sum(data['f'] **2) - (np.sum(data['f']))**2
A2 = (N * np.sum(data['f'] * phi) - np.sum(data['f']) * np.sum(phi)) / Delta
B2 = (np.sum(data['f']**2) * np.sum(phi) - np.sum(data['f']) * np.sum(data['f'] * phi)) / Delta

plt.plot(data['f'], phi, 'r.', label = 'Messwerte')
#plt.plot(data['f'], A2*data['f'] + B2, 'b', label='lineare Regression')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$\varphi(f)$')
#plt.ylabel(r'$a \:/\:$ ms')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotbc3.pdf')
plt.clf()

#plt.plot(data['f'], data['b'], 'r.', label = r'$b \:/\:$ ms')
#plt.xlabel(r'$f \:/\:$ kHz')
#plt.ylabel(r'$b \:/\:$ ms')
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/plotbc4.pdf')
#plt.clf()