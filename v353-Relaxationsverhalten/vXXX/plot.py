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


#Beginn Plot zu Aufgabenteil a)
daten = np.genfromtxt('../Dateien/Aufgabea.txt', delimiter=';', names=True)

x1 = daten['U'] +2.5
x = np.log(x1)
y = daten['t']
T = unp.uarray(daten['t'],0.1) #Fehler von t
U = unp.uarray(x1,0.1) #Fehler von U

m , b , r ,p ,std =stats.linregress(y,x)
M=unp.uarray(m,std)
B=unp.uarray(b,std)



N = len(y)
Delta = N * np.sum(y**2) - (np.sum(y))**2

A = (N * np.sum(x * y) - np.sum(y) * np.sum(x)) / Delta
B = (np.sum(y**2) * np.sum(x) - np.sum(y) * np.sum(x * y)) / Delta
#print('Steigung für Aufgabenteil a) beträgt:', A)
#print('y-Achsenabschnitt für Aufgabenteil a) beträgt:', B)
#print(m*daten['t']+b)
#print(x)
#print(m)
#print(b)

plt.plot(y,x, '.', color = 'crimson', label = 'Messwerte')
#plt.errorbar(y,x, xerr = stds(T), yerr = stds(unp.log(U/5)), fmt = '.', color = 'crimson', label = 'Messwerte')
plt.plot(daten['t'], m*daten['t']+b, color = 'mediumblue', label='Fit')
#plt.plot(x, A*x + B, color = 'mediumblue', label='lineare Regression')
plt.legend()
plt.ylabel(r'$ U \:/\:$ V')
plt.xlabel(r'$t \:/\:$ ms')
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

plt.plot(w, relAmp, '.', color = 'crimson', label = 'Messwerte')
#plt.plot(data['f'], A1*data['f'] + B1, 'b', label='lineare Regression')

parameters, pcov = curve_fit(f1, w , data['A2']/4.2, sigma=None, p0=0)
RC_B=unp.uarray(parameters,pcov)
#print(f'RC_b = {RC_B*10**6} [\mu s]')
#print(f'RC_b = {parameters*10**3} [\mu s]')
#plt.xscale('log')
xx = np.linspace(w[0], w[19], 20)
plt.plot(xx, f1(xx,*parameters), color = 'mediumblue', label='Fit')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$A(\omega)/U_0$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.savefig('build/plotb.pdf')
plt.clf()


#Plot zu Aufgabenteil c)

phi =  data['a']/data['b']
#print(phi)
plt.plot(data['f'], phi, '.', color = 'dodgerblue', label = r'Messwerte')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$\varphi(f)\:/\:$ rad')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotc.pdf')
plt.clf()



#Theorieplot
x = np.linspace(3,60,200)
y = np.arctan(-x*1.6)
a=0.3
plt.plot(x, -y, color = 'limegreen', label = r'Theoriekurve')
plt.legend(loc='best')
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$\varphi(f)$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Theorieplot.pdf')
plt.clf()

#Polarplot
phi2 = np.linspace(0.0, (np.pi)/2.0, 20)
plt.polar(phi, data['A2'], '.', color = 'darkviolet', label = r'Messwerte')
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