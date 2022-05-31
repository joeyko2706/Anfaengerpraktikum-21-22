import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const
import scipy.optimize as op
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


U, I, z = np.genfromtxt("data/ersterStoff.txt", unpack = True)

n = np.sqrt(z)
plt.errorbar(U, z, yerr = n, fmt = "gx")

plt.savefig("build/plot.pdf")