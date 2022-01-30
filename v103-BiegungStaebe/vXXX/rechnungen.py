import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import scipy.optimize as opt

gewichtsKr_eins = 7.3575    #750g
gewichtsKr_beids = 15.2055  #1550g


#Masse des eckigen Stabes

masse_eckig_gramm = np.array([535.4, 536.2, 536.1, 535.7, 536.3])
masse_eckig = masse_eckig_gramm / 1000
print('Mittelwert Masse eckig:', np.round(np.mean(masse_eckig), 4), '\n Abweichung: ', np.round(np.std(masse_eckig), 4))

m_e = ufloat(np.round(np.mean(masse_eckig), 4),  np.round(np.std(masse_eckig), 4))

#Volumen eckiger Stab

a_eckig = np.array([0.602, 0.602, 0.602, 0.602, 0.602])
l = np.array([0.01, 0.01, 0.01, 0.01, 0.01])
volumen_eckig = a_eckig * l * l
dichte_eckig = masse_eckig/volumen_eckig
print('Dichte eckiger Stab:', np.round(np.mean(dichte_eckig), 4), '+-', np.round(np.std(dichte_eckig), 4))



#Flächenträgheitsmoment eckiger Stab

a_mm = np.array([10.0, 10.0, 10.0, 10.0, 10.0])
a_rund = ufloat(np.round(np.mean(a_mm*10**(-3)), 4), np.round(np.std(a_mm*10**(-3)), 4))
print('Trägheitsmoment eckiger Stab: ', 1/12* a_rund)

#Elasti 1 eckig
steigung1 = ufloat(0.0297, 0.0004)
traegheit1 = ufloat(0.83, 0)
print('Elasti eckig einseitig: ', gewichtsKr_eins/ (2*traegheit1*steigung1))

#Elasti2 eckig
steigung2 = ufloat(0.00266, 0.00012)
steigung3 = ufloat(-0.001, 0.004)
print('Elasti eckig beidseitig1:', gewichtsKr_beids / (48*traegheit1*steigung2) )
print('Elasti eckig beidseitig2:', gewichtsKr_beids / (48*traegheit1*steigung3) )

#Masse/Länge des runden Stabes
masse_rund_gramm = np.array([411.8, 412.0, 412.2, 412.2, 412.2])
masse_rund = masse_rund_gramm / 1000
m_r = ufloat(np.round(np.mean(masse_rund), 4), np.round(np.std(masse_rund), 4))

laenge_rund_centi =  np.array([59.3, 59.2, 59.2, 59.2, 59.1])
laenge_rund = laenge_rund_centi / 100
print('Mittelwert Masse rund:', np.round(np.mean(masse_rund), 4), '\n Abweichung: ', np.round(np.std(masse_rund), 4))
print('Mittelwert Länge rund:', np.round(np.mean(laenge_rund), 4), '\n Abweichung: ', np.round(np.std(laenge_rund), 4))

#Dichte runder Stab

flaeche_kreis = np.pi * (a_mm/1000) ** 2
volumen_rund= flaeche_kreis * laenge_rund
dichte_rund = masse_rund / volumen_rund
print('Dichte runder Stab: ', np.round(np.mean(dichte_rund), 4),'+-' , np.round(np.std(dichte_rund), 4) )


#Elasti 1 rund
steigung1_rund = ufloat(0.0455, 0.0007)
gewichtskraft_rund = ufloat(4.0427 ,0.002)
traegheit_rund = ufloat( ((1*10**(-2))**4 * np.pi )/ 64 , 0.0 )
print('Elasti rund einseitig: ', gewichtsKr_eins/ (2*traegheit_rund*steigung1_rund))

#Elastis rund
steigung2_rund = ufloat(0.00376, 0.00023)
steigung3_rund = ufloat(0.00587, 0.00031)
print('Elasti rund beidseitig 1: ', gewichtsKr_beids/ (48*traegheit_rund*steigung2_rund))
print('Elasti rund beidseitig 2: ', gewichtsKr_beids/ (48*traegheit_rund*steigung3_rund))

#ElastiMittel1 ohne den doofen 1en Wert
elasti_gesamt1 = 1/2 * (gewichtsKr_eins/ (2*traegheit1*steigung1) + gewichtsKr_beids / (48*traegheit1*steigung2))
print('Mittelwert Elastizität eckig: ', elasti_gesamt1)

#ElastiMittel2
elasti_gesamt2 = 1/3 * (gewichtsKr_eins/ (2*traegheit_rund*steigung1_rund) + gewichtsKr_beids/ (48*traegheit_rund*steigung2_rund) + gewichtsKr_beids/ (48*traegheit_rund*steigung3_rund))
print('Mittelwert Elastizität rund: ', elasti_gesamt2)