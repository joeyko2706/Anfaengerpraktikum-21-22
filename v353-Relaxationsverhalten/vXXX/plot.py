import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unp
from scipy import stats
from scipy.optimize import curve_fit
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import numpy as np
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

print(r'Plots werden durchgegangen')

daten = np.genfromtxt('../Dateien/Aufgabea.txt', delimiter=';', names=True)

x1 = daten['U'] +2.5
x = np.log(x1)
y = daten['t']

N = len(y)
Delta = N * np.sum(x**2) - (np.sum(x))**2

A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta
#print('Steigung für Aufgabenteil a) beträgt:', A)
#print('y-Achsenabschnitt für Aufgabenteil a) beträgt:', B)

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
relAmp = data['A2']/data['A1']
w = 2*np.pi*data['f']
#print('Relativamplitude beträgt:', relAmp)

def f1(w,c):
    return 1/(np.sqrt(1+(w**2 * c**2)))

plt.plot(w, relAmp, 'r.', label = 'Messwerte')
#plt.plot(data['f'], A1*data['f'] + B1, 'b', label='lineare Regression')

parameters, pcov = curve_fit(f1, w , data['A2']/4.2, sigma=None, p0=0)
RC_B=unp.uarray(parameters,pcov)
#print(f'RC_b = {RC_B*10**6} [\mu s]')
#print(f'RC_b = {parameters*10**3} [\mu s]')
#plt.xscale('log')
xx = np.linspace(w[0], w[19], 20)
plt.plot(xx, f1(xx,*parameters), 'b', label='Fit')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$A/U_0$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.savefig('build/plotb.pdf')
plt.clf()


#Plot zu Aufgabenteil c)

phi =  data['a']/data['b']
#print(phi)
plt.plot(data['f'], phi, '*', color = 'dodgerblue', label = r'Messwerte')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$\varphi(f)$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotc.pdf')
plt.clf()



#Theorieplot
x = np.linspace(3,60,200)
xx = np.linspace((np.e)**5, (np.e)**14, 10000)
a=0.3
plt.plot(x, np.arctan(x*a-1.8), label = r'Theoriekurve')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$\varphi(f)$')
plt.savefig('build/Theorieplot.pdf')
plt.clf()

#Polarplot
phi2 = np.linspace(0.0, (np.pi)/2.0, 20)
plt.polar(phi, data['A2'], '*', color = 'darkviolet', label = r'Messwerte')
plt.polar(phi2, np.cos(phi2), color='navy', label = r'Theoriekurve')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotd.pdf')
plt.clf()




#fig = plt.figure()
#ax1 = plt.subplot(121, projection = 'polar')
#ax2 = plt.subplot(122, projection='polar')
#
#ax1.scatter(phi, data['A2'], '*', color = 'darkviolet', label = r'Messwerte')
#ax2.scatter(phi2, np.cos(phi2), color='navy', label = r'Theoriekurve')
#plt.show()

print('Fertig')