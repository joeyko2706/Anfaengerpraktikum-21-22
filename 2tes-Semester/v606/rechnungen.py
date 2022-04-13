import numpy as np
from uncertainties import ufloat

#Konstanten und andere feste Werte

mu_0 = 4 * np.pi *10**(-7) #magnetische Feldkonstante
k = 1.380650 * 10**(-23) #Boltzmann Konstante
T = 295.15 #Raumtemperatur (ungefähr)
mu_b = 9.2740100784 * 10**(-24) #Bohr'sches Magneton
faktor = (mu_0 * (mu_b)**2)/(3*k*T) #Faktor für den theoretischen Wert der Suszeptibilittät
print(f'Faktor = ', faktor)

#-------------- Theoretische magnetische Suszeptibilität

J_Nd = 9/2
S_Nd = 3/2
L_Nd = 6.0
g_Nd = ( 3 * J_Nd * (J_Nd+1) + S_Nd * (S_Nd+1)-L_Nd* (L_Nd + 1) ) / (2* J_Nd * (J_Nd + 1))
N_Nd = 2.591 * 10**(22)
chi_NdTheo = faktor * N_Nd * J_Nd * (g_Nd)**2 * (J_Nd + 1)

J_Gd = 7/2
S_Gd = 7/2
L_Gd = 0
g_Gd = ( 3* J_Gd * (J_Gd+1) + S_Gd * (S_Gd+1)-L_Gd* (L_Gd+1) )/(2* J_Gd * (J_Gd + 1))
N_Gd = 2.458 * 10**(22)
chi_GdTheo = faktor * N_Gd * J_Gd * (g_Gd)**2 * (J_Gd + 1)

J_Dy = 15/2
S_Dy = 5/2
L_Dy = 5
g_Dy = ( 3* J_Dy * (J_Dy+1) + S_Dy * (S_Dy+1)-L_Dy * (L_Dy+1) )/(2* J_Dy * (J_Dy + 1))
N_Dy = 2.029 * 10**(22)
chi_DyTheo = faktor * N_Dy * J_Dy * (g_Dy)**2  * (J_Dy + 1)

print(f'Neodym g: ', g_Nd)  #Richtiger Wert
print(f'Gadolinium g: ', g_Gd)  #Richtiger Wert
print(f'Dysprosium g: ', g_Dy)  #Richtiger Wert
print(f'Magn Susz fuer Neodym: ',chi_NdTheo, '\t' )
print(f'Magn Susz fuer Gadolinium: ',chi_GdTheo, '\t' )
print(f'Magn Susz fuer Dysprosium: ',chi_DyTheo, '\t' )
print('---------')


#---------------------------
deltarnd = np.array([0.175, 0.2, 0.19])
deltargd = np.array([0.9, 0.9, 0.8])
deltardy = np.array([1.675, 1.675, 1.675])
brueckenspgd = np.array([67.0, 69.0, 69.0])

deltaRnd = ufloat(np.round(np.mean(deltarnd), 4), np.round(np.std(deltarnd), 4))
deltaRgd = ufloat(np.round(np.mean(deltargd), 4), np.round(np.std(deltargd), 4))
deltaRdy = ufloat(np.round(np.mean(deltardy), 4), np.round(np.std(deltardy), 4))
BrueckenspGd = ufloat(np.round(np.mean(brueckenspgd), 4), np.round(np.std(brueckenspgd), 4))

print('Delta R für Neodym:', deltaRnd)
print('Delta R für Geodinium:', deltaRgd)
print('Delta R für Dysprosium:', deltaRdy)
print('Brückenspannung für Geodinium:', BrueckenspGd)
print('---------')


#---------------- Suszeptibilität nach erster Art
L = 13.5 *10**(-2) #Länge der Spule

m_Nd = 8.48 *10**(-3)#Massen in kg
m_Gd = 14.08 *10**(-3)
m_Dy = 15.1 *10**(-3)

rho_Nd = 7.24 *1000 #Einkristalldichten in kg/m^3
rho_Gd = 7.4 *1000
rho_Dy = 7.8 *1000

Q_Nd = m_Nd/(L * rho_Nd) #effektive Querschnittsfläche in m^2
Q_Gd = m_Gd/(L * rho_Gd)
Q_Dy = m_Dy/(L * rho_Dy)

F = 86.6 * 10**(-6) #Querschnitt der Spule in m

chi_ersteNd = (4 * F * 49 * 10**(-3)) / (Q_Nd)
chi_ersteGd = (4 * F * BrueckenspGd * 10**(-3)) / (Q_Gd)
chi_ersteDy = (4 * F * 30.75 * 10**(-3)) / (Q_Dy)

print(f'effektiver Querschnitt Neodym: ', Q_Nd)
print(f'effektiver Querschnitt Gadolinium: ', Q_Gd)
print(f'effektiver Querschnitt Dysprosium: ', Q_Dy)

print(f'Erste Suszeptibilität Neodym: ', chi_ersteNd)
print(f'Erste Suszeptibilität Gadolinium: ', chi_ersteGd)
print(f'Erste Suszeptibilität Dysprosium: ', chi_ersteDy)
print('---------')

#------------- Suszeptibilität nach zweiter Art
R_a = 998.925

chi_zweiteNd = (2 * deltaRnd * F) / (R_a * Q_Nd)
chi_zweiteGd = (2 * deltaRgd * F) / (R_a * Q_Gd)
chi_zweiteDy = (2 * deltaRdy * F) / (R_a * Q_Dy)

print(f'Zweite Suszeptibilität Neodym: ', chi_zweiteNd)
print(f'Zweite Suszeptibilität Gadolinium: ', chi_zweiteGd)
print(f'Zweite Suszeptibilität Dysprosium: ', chi_zweiteDy)