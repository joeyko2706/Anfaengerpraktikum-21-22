import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

c = const.c
h = const.h
d = 201.4 * 10**(-12) 
e = const.e


def f(E):
    a = np.arcsin((h*c)/(2 * d * E * e))
    return np.rad2deg(a)


print("Winkel Germanium:", f(11114)) #bereits in eV
print("Winkel Brom:", f(13484))
print("Winkel Rubidium :", f(15208))
print("Winkel Strontium :", f(16115))
print("Winkel Zirconium:", f(18008))
print("Winkel Gallium:", f(10368))