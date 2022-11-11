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

#Einfügen der Daten
B=np.array([3, 104, 276, 394, 475, 531, 576, 610, 642, 668, 696, 682, 667, 648, 626, 600, 566, 523, 460, 342, 131, -70, -147, -380, -472, -531, -578, -614, -646, -674, -700, -691, -676, -655, -632, -603, -570, -523, -457, -333, -123, 78, 267, 400, 485, 544, 589, 625, 655, 684, 715])
I=np.array([0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])

#magnetische Feldstärke der Spule nach Formel (5) bestimmen
my_0=4*np.pi*10**(-7)
n=595
r=0.135
H_Faktor=n*(2*np.pi*r)**(-1)
H_Spule=H_Faktor * I

B_Magnetisierung=(B*10**(-3)*(my_0)**(-1)-H_Spule)*my_0*10**3 


#Remanenz:
plt.plot(H_Spule[20:21],B_Magnetisierung[20:21],'k*',label='Remanenz')
plt.plot(H_Spule[40:41],B_Magnetisierung[40:41],'k*')

#Sättigung
plt.plot(H_Spule[10:11],B_Magnetisierung[10:11],'m*',label='Sättigung')
plt.plot(H_Spule[30:31],B_Magnetisierung[30:31],'m*')

#Koerzitivkraft:
plt.plot(H_Spule[20:21],B_Magnetisierung[20:21],'y*',label='Koerzitivkraft')
# print(H_Spule[20:21], B_Magnetisierung[220:21])

#Neukurve:
plt.plot(H_Spule[0:10], B_Magnetisierung[0:10], 'b.', label = 'Neukurve')

#Kurvenverlauf 2:
plt.plot(H_Spule[10:30], B_Magnetisierung[10:30], 'g.', label = 'Kurve 2')

#Kurvenverlauf 3:
plt.plot(H_Spule[30:50], B_Magnetisierung[30:50], 'r.', label = 'Kurve 3')


plt.xlabel(r'$H\,/\,\si{\ampere\per\meter}$')
plt.ylabel(r'$B\,/\,$ mT')
plt.grid()
plt.legend()
plt.savefig('hysterese.pdf')