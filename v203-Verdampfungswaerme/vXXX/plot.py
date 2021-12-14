import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

#x = np.linspace(0, 10, 1000)
#y = x ** np.sin(x)

#plt.subplot(1, 2, 1)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

#x=np.array([2, 5, 6.5])
#y= 1/x



T=np.array([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,62,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84])
x=(1/(T+273.15))*100
P= np.array([38,39,39,43,44,46,47,49,50,52,53,55,57,59,60,63,65,67,69,73,77,81,85,90,94,99,104,109,115,122,128,132,138,146,160,168,195,205,222,237,255,267,277,290,301,315,328,342,355,370,383,395,376,385,396,409,420,435,453,463])
y= np.log(P/993)

N = len(y)
Delta = N * np.sum(x**2) - (np.sum(x))**2

A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
B = (np.sum(x**2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

sigma_y = np.sqrt(np.sum((y - A * x - B)**2) / (N - 2))

A_error = sigma_y * np.sqrt(N / Delta)
B_error = sigma_y * np.sqrt(np.sum(x**2) / Delta)

#print(A, A_error, B, B_error)
plt.figure()
plt.plot(x, y,  '.', label='Messwerte')
plt.plot(x, A*x + B, 'r', label='lineare Regression')
plt.xlabel(r'$\frac{1}{T} \:/\: \frac{1}{10^3 \cdot K}$')
plt.ylabel(r'$ln\left(\frac{p}{p_0}\right) $')
plt.grid()
plt.legend()
# in matplotlibrc leider (noch) nicht möglich
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')




T=np.array([116,133,141,149,156,163,168,173,176,181,185,188,191,194,197])
y=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
x= T+273.15

def f(x, a, b, c, d):
    return a*x**3+b*x**2+c*x+d
popt, pcov = curve_fit(f, x, y)
print(popt)

plt.figure()
plt.plot(x, f(x, *popt), 'r', label='Regressionspolynom')
plt.plot(x, y,  '.', label='Messwerte')
plt.xlabel("T [K]")
plt.ylabel("p [Pa] $\cdot 10^5$")
plt.grid()
plt.legend()
plt.savefig('build/plot2.pdf')

