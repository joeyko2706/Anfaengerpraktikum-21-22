import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import scipy.optimize as opt

#Masse des eckigen Stabes

masse_eckig_gramm = np.array([534.4, 536.2, 536.1, 535.7, 536.3])
masse_eckig = masse_eckig_gramm / 1000
print('Mittelwert Masse eckig:', np.round(np.mean(masse_eckig), 4), '\n Abweichung: ', np.round(np.std(masse_eckig), 4))

#Gewichtskraft eckiger Stab

g=9.81
m_e = ufloat(np.round(np.mean(masse_eckig), 4),  np.round(np.std(masse_eckig), 4))
print('Gewichtskraft des eckigen Stabes:', g*m_e)

#Flächenträgheitsmoment eckiger Stab

a_mm = np.array([10.0, 10.0, 10.0, 10.0, 10.0])
a = ufloat(np.round(np.mean(a_mm*10**(-3)), 4), np.round(np.std(a_mm*10**(-3)), 4))
print('Trägheitsmoment eckiger Stab: ', 1/12*a)

#Elasti 1
steigung1 = ufloat(0.0297, 0.0004)
gewichtskraft1 = ufloat(5.255 ,0.007)
traegheit1 = ufloat(0.83, 0)
print('Elasti eckig einseitig: ', gewichtskraft1/ (2*traegheit1*steigung1))

#Elasti2
steigung2 = ufloat(0.00266, 0.00012)
steigung3 = ufloat(-0.001, 0.004)
print('Elasti eckig beidseitig1', gewichtskraft1 / (48*traegheit1*steigung2) )
print('Elasti eckig beidseitig2', gewichtskraft1 / (48*traegheit1*steigung3) )