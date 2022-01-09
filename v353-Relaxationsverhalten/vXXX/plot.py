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

y1 = daten['U'] +2.5
y = np.log(y1)
x = daten['t']
T = unp.uarray(daten['t'],0.1) #Fehler von t
U = unp.uarray(y1,0.1) #Fehler von U

m , b , r ,p ,std =stats.linregress(x,y)
M=unp.uarray(m,std)
B=unp.uarray(b,std)



N = len(y)
Delta = N * np.sum(y**2) - (np.sum(y))**2

A_man = (N * np.sum(x * y) - np.sum(y) * np.sum(x)) / Delta
B_man = (np.sum(y**2) * np.sum(x) - np.sum(y) * np.sum(x * y)) / Delta

sigma_y = np.sqrt(np.sum((y - A_man * x - B_man)**2) / (N - 2))
A_error = sigma_y * np.sqrt(N / Delta)
B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)
#print('A_error = ',A_error) #Unsicherheit auf der Steigung auf der manuell berechneten Ausgleichsgeraden
#print('B_error = ', B_error)    #Unsicherheit auf des  y-Achsenabschnitts auf der manuell berechneten Ausgleichsgeraden  
#print('Steigung für Aufgabenteil a) beträgt:', A)   #Steigung auf der manuell berechneten Ausgleichsgeraden 
#print('y-Achsenabschnitt für Aufgabenteil a) beträgt:', B)  #y-Achsenabschnitt auf der manuell berechneten Ausgleichsgeraden 

#print(f'RC_a = {-1/M} [\mu s]') #Durch CorveFit ermittelte Zeitkonstante RC
#print(f'Steigung aus CurveFit: f{M}')   #Durch CurveFit ermittelte Steigung der Ausgleichsgeraden
#print(f'y-Achsenabschnitt aus CurveFit: {B}')   #Durch CurveFit ermittelter y-Achsenabschnitt der Ausgleichsgeraden

plt.plot(x, y, '.', color = 'crimson', label = 'Messwerte')
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
#print(f'RC_b = {RC_B*10**3} [\mu s]')   #Zeitkonstante RC mit Unsicherheit(wahrscheinlich ohne "*10**3" richtig!)
#print(f'RC_b = {parameters*10**3} [\mu s]') #Zeitkonstante RC ohne Unsicherheit(wahrscheinlich ohne "*10**3" richtig!)
xx = np.linspace(w[0], w[19], 20)
plt.plot(xx, f1(xx,*parameters), color = 'mediumblue', label='Fit')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$A(\omega)/U_0$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.savefig('build/plotb.pdf')
plt.clf()


#Plot zu Aufgabenteil c)

phi =  data['a']/data['b']  #Phasenverschiebung -> Messwerte sind nicht gut!
#print(phi)
plt.plot(data['f'], phi, '.', color = 'dodgerblue', label = r'Messwerte')
plt.legend()
plt.xlabel(r'$f \:/\:$ kHz')
plt.ylabel(r'$\varphi(f)\:/\:$ rad')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotc.pdf')
plt.clf()



#Theorieplot (Wie Plot c eigentlich hätte aussehen sollen mit RC = 1.6)
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
plt.polar(phi2, np.cos(phi2), color='navy', label = r'Theoriekurve')    #Theoriekurve wird nicht in dem Polarplot angezeigt
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plotd.pdf')
plt.clf()


#Versuch 2 Plots in einen Polarplot zu bekommen und sich ausgeben zu lassen.
#X-Server muss vorher gestartet werden.

#fig = plt.figure()
#ax1 = plt.subplot(121, projection = 'polar')
#ax2 = plt.subplot(122, projection='polar')
#
#ax1.scatter(phi, data['A2'], '*', color = 'darkviolet', label = r'Messwerte')
#ax2.scatter(phi2, np.cos(phi2), color='navy', label = r'Theoriekurve')
#plt.show()

print('Fertig')