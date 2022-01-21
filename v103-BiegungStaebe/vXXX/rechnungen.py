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