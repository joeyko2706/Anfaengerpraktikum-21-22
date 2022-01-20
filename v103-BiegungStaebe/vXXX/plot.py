import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unp
from scipy import stats
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

print(r'Plots werden durchgegangen')

####################################
#Eckiger Stab einseitige Einspannung

x1, y1 = np.genfromtxt('../Dateien/aquadr1.txt', unpack = True)    #quadratischer Stab ohne Last
x2, y2 = np.genfromtxt('../Dateien/aquadr2.txt', unpack = True)    #quadratischer Stab mit Last
x = x1 *10**(-2)

L = 0.602
Eta = L*x**2-(1/3)*x**3
D_X = (y1 - y2)*10**(-3)
m_eckig_einseitig , b_eckig_einseitig , r ,p ,std =stats.linregress(noms(Eta),noms(D_X))
M_eckig_einseitig=unp.uarray(m_eckig_einseitig,std) #M mit Fehler
B_eckig_einseitig=unp.uarray(b_eckig_einseitig,std) #B mit Fehler
X = np.linspace(0, 0.102, 100)

#print(f'M rund einseitig: {M_eckig_einseitig}')
#print(f'B rund einseitig: {B_eckig_einseitig}')
#print(f'Eta: {Eta} \n D(x): {D_X}')

plt.plot(X,m_eckig_einseitig*X+b_eckig_einseitig, color = 'mediumblue', label = 'Fit')
plt.plot(noms(Eta), D_X, '.', color = 'crimson', label = 'Messdaten')

plt.legend(loc = 'best')
plt.xlabel(r'$\eta(x)$ / \unit{\cubic\meter}$')
plt.ylabel(r'$D(x)$ / $\unit{\meter}$')
#plt.xlim(0.0, 0.11)
#plt.ylim(0.0, 0.0031)
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')  #Plot des quadratischen Stabes bei einseitiger Einspannung
plt.clf()

##########################################
#Eckiger Stab beidseitig eingespannt

L = 0.602
x3, y3 = np.genfromtxt('../Dateien/bquadr1a.txt', unpack = True) #Quadratischer Stab beidseitig ohne Last, erste Hälfte
x4, y4 = np.genfromtxt('../Dateien/bquadr2a.txt', unpack = True) #Quadratischer Stab beidseitig mit Last, erste Hälfte
X2 = x3*10**(-2)

Eta_1 = 3*L**2*X2-4*X2**3
D1_X = (y3-y4)*10**(-3)

m1_eckig_beidseitig , b1_eckig_beidseitig , r ,p ,std =stats.linregress(noms(Eta_1),noms(D1_X)) #Erster Fit
M1_eckig_beidseitig=unp.uarray(m1_eckig_beidseitig,std) #M1 mit Fehler
B1_eckig_beidseitig=unp.uarray(b1_eckig_beidseitig,std) #B1 mit Fehler
X1 = np.linspace(0, 0.22, 100)


x5, y5 = np.genfromtxt('../Dateien/bquadr1b.txt', unpack = True) #Quadratischer Stab beidseitig ohne Last, zweite Hälfte
x6, y6 = np.genfromtxt('../Dateien/bquadr2b.txt', unpack = True) #Quadratischer Stab beidseitig mit Last, zweite Hälfte
X3 = x5 *10**(-2)

Eta_2 = 4*X3**3 - 12*L*X3**2 + 9*L**2*X3 - L**3
D2_X = (y5-y6)*10**(-3)
m2_eckig_beidseitig , b2_eckig_beidseitig , r ,p ,std =stats.linregress(noms(Eta_2),noms(D2_X)) #Zweiter Fit

M2_eckig_beidseitig=unp.uarray(m2_eckig_beidseitig,std) #M2 mit Fehler
B2_eckig_beidseitig=unp.uarray(b2_eckig_beidseitig,std) #B2 mit Fehler

plt.subplot(1,2,1)
plt.plot(noms(Eta_1), noms(D1_X), '.', color = 'crimson', label = 'Messdaten 1')
plt.plot(X1,m1_eckig_beidseitig*X1+b1_eckig_beidseitig ,color = 'mediumblue', label = 'Fit 1')
plt.xlabel(r'$\eta(x)$ / $\unit{\cubic\meter}$')
plt.ylabel(r'$D(x)$ / $\unit{\meter}$')
plt.legend(loc='best')
plt.grid()

plt.subplot(1,2,2)
plt.plot(noms(Eta_2), noms(D2_X), '.', color = 'crimson' , label='Messdaten 2')
plt.plot(X1,m2_eckig_beidseitig*X1+b2_eckig_beidseitig, color = 'mediumblue', label = 'Fit 2')  
plt.xlabel(r'$\eta(x)$ / \unit{\cubic\meter}$')
plt.ylabel(r'$D(x)$ / $\unit{\meter}$')
plt.legend(loc='best')
plt.grid()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.clf()

#########################
#Runder Stab einseitige Einspannung

L1 = 0.59
xr0 , yr0 = np.genfromtxt('../Dateien/azyl1.txt', unpack = True)  #Runder Stab bei einseitiger Einspannung ohne Last
xr1, yr1 = np.genfromtxt('../Dateien/azyl2.txt', unpack = True)   #Runder Stab bei einseitiger Einspannung mit Last
Xr = xr0 *10**(-2)


Eta_r0 = L1*Xr**2-(1/3)*Xr**3
DR0_X = (yr0-yr1) *10**(-3)
m_rund_einseitig , b_rund_einseitig , r ,p ,std =stats.linregress(noms(Eta_r0),noms(DR0_X))

M_rund_einseitig=unp.uarray(m_rund_einseitig,std) #M mit Fehler
B_rund_einseitig=unp.uarray(b_rund_einseitig,std) #B mit Fehler
X = np.linspace(0, 0.102, 100)

plt.plot(noms(Eta_r0), DR0_X, '.', color = 'crimson', label = 'Messdaten')
plt.plot(X,m_rund_einseitig*X+b_rund_einseitig, color = 'mediumblue', label = 'Fit')


plt.legend(loc = 'best')
plt.xlabel(r'$\eta(x)$ / \unit{\cubic\meter}$')
plt.ylabel(r'$D(x)$ / $\unit{\meter}$')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')  #Plot des runden Stabes bei einseitiger Einspannung
plt.clf()

#############################
#Runder Stab beidseitig eingespannt

#Werte
xr2, yr2 = np.genfromtxt('../Dateien/bzyl1a.txt', unpack = True) #Zylindrischer Stab beidseitig ohne Last, erste Hälfte
xr3, yr3 = np.genfromtxt('../Dateien/bzyl2a.txt', unpack = True) #Zylindrischer Stab beidseitig mit Last, erste Hälfte
XR1 = xr2 *10**(-2)

xr4, yr4 = np.genfromtxt('../Dateien/bzyl1b.txt', unpack = True) #Zylindrischer Stab beidseitig ohne Last, zweite Hälfte
xr5, yr5 = np.genfromtxt('../Dateien/bzyl2b.txt', unpack = True) #Zylindrischer Stab beidseitig mit Last, zweite Hälfte
XR2 = xr4 *10**(-2)

Eta_r1 = 3*L1**2*XR1-4*XR1**3
Eta_r2 = 4*XR2**3 - 12*L1*XR2**2 + 9*L1**2*XR2 - L1**3
DR1_X = (yr2-yr3) *10**(-3)
DR2_X = (yr4-yr5) *10**(-3)

m1_rund_beidseitig , b1_rund_beidseitig , r ,p ,std =stats.linregress(noms(Eta_r1),noms(DR1_X)) #Erster Fit
M1_rund_beidseitig=unp.uarray(m1_rund_beidseitig,std) #M1 mit Fehler
B1_rund_beidseitig=unp.uarray(b1_rund_beidseitig,std) #B1 mit Fehler

m2_rund_beidseitig , b2_rund_beidseitig , r ,p ,std =stats.linregress(noms(Eta_r2),noms(DR2_X)) #Zweiter Fit
M2_rund_beidseitig=unp.uarray(m2_rund_beidseitig,std) #M2 mit Fehler
B2_rund_beidseitig=unp.uarray(b2_rund_beidseitig,std) #B2 mit Fehler
XR = np.linspace(0, 0.22, 100)

#Plot
plt.subplot(1,2,1)
plt.plot(noms(Eta_r1), noms(DR1_X), '.', color = 'crimson', label = 'Messdaten 1')
plt.plot(XR,m1_rund_beidseitig*XR+b1_rund_beidseitig ,color = 'mediumblue', label = 'Fit 1')
plt.xlabel(r'$\eta(x)$ / $\unit{\cubic\meter}$')
plt.ylabel(r'$D(x)$ / $\unit{\meter}$')
plt.legend(loc='best')
plt.grid()

plt.subplot(1,2,2)
plt.plot(noms(Eta_r2), noms(DR2_X), '.', color = 'crimson' , label='Messdaten 2')
plt.plot(XR,m2_rund_beidseitig*XR+b2_rund_beidseitig, color = 'mediumblue', label = 'Fit 2')  
plt.xlabel(r'$\eta(x)$ / \unit{\cubic\meter}$')
plt.ylabel(r'$D(x)$ / $\unit{\meter}$')
plt.legend(loc='best')
plt.grid()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot4.pdf')
plt.clf()

print('Plots fertig')