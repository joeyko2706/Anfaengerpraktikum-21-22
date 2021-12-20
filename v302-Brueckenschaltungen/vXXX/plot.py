import matplotlib.pyplot as plt
import numpy as np

f = np.array([20,40,80,160,180,200,220,230,235,240,245,250,260,280,300,320,340,640,1280,2560,5120,10240,20480,30000])
U = np.array([300,280,210,75,50,34,16,7,5,0,5,7,15,30,45,60,65,170,250,250,250,250,200,140])
x = f/240
y = U/(1000*2.83)

#plt.subplot(1, 2, 1)
plt.plot(x, y, '.', label='Messwerte')
plt.plot(x, (1)/(9) * ((x**2 -1)**2)/(((1-x**2)**2)+9*x**2), label='Theoriekurve')
plt.xscale('log')
plt.xlim(10**(-1), 10**(2.15))
plt.ylabel(r'$\frac{U_{Br}}{U_{S}}$')
plt.xlabel(r'$\frac{f}{f_0}$')
plt.grid()
plt.legend(loc='best')

#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
