import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
import numpy as np
mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})

#Für Theoriekurve:
my_0=4*np.pi*10**(-7)
I = 4.5
n = 100
R = 62.5 *10**(-3)
faktor = 0.5*my_0 *I*R*R
d1=273 *10**(-3)#mm
d2 = 198 *10**(-3)#mm
d3 = 143 *10**(-3)#mm




#Spulenpaar 1

x1 = np.array([250, 180, 160, 140, 120, 100, 80, 60, 40, 20, -50])
B1 = np.array([3.097, 2.917, 2.024, 1.414, 1.086, 0.984, 1.067, 1.364, 1.936, 2.792, 3.002])
z = np.linspace(-50,250)

plt.xlabel('Abstand $x$ / mm')
plt.ylabel('$B$ / mT')
plt.plot(x1, B1, 'r.', label = 'Messwerte')
plt.plot(z,10**8*faktor*(R*R + (z-0.5*d1)**2)**(-1.5) + 10**8*faktor*(R*R + (z+0.5*d1)**2)**(-1.5),label='Theoriekurve')


plt.legend(loc='lower left')
plt.savefig('Spulenpaar1.pdf')

#Spulenpaar 2
plt.clf()

x = np.array([240, 220, 140, 120, 100, 80, 60, 40, 20])
B = np.array([1.728, 2.640, 3.038, 2.182, 1.651, 1.475, 1.617, 2.105, 2.916])
z = np.linspace(20,240)


plt.xlabel('Abstand $x$ / mm')
plt.ylabel('$B$ / mT')
plt.plot(x, B, 'g.', label = 'Messwerte')
plt.plot(z,10**8*faktor*(R*R + (z-0.5*d2)**2)**(-1.5) + 10**8*faktor*(R*R + (z+0.5*d2)**2)**(-1.5),label='Theoriekurve')

plt.legend()
plt.savefig('Spulenpaar2.pdf')

#Spulenpaar 3
plt.clf()


x = np.array([170, 155, 90, 75, 60, 45, 30, 15])
B = np.array([2.478, 3.268, 3.646, 3.088, 2.769, 2.742, 3.025, 3.547])
z = np.linspace(15,170)


plt.xlabel('Abstand $x$ / mm')
plt.ylabel('$B$ / mT')
plt.plot(x, B, 'm.', label = 'Messwerte')
plt.plot(z,10**8*faktor*(R*R + (z-0.5*d3)**2)**(-1.5) + 10**8*faktor*(R*R + (z+0.5*d3)**2)**(-1.5),label='Theoriekurve')

plt.legend()
plt.savefig('Spulenpaar3.pdf')