import matplotlib.pyplot as plt
import numpy as np
import uncertainties as uc
import scipy.constants as const

difference=np.array(np.zeros(25))

def generatediffernce(y):
    for i in range(25):
        difference[i]=y[i+1]-y[i]
    return difference

xrt,yrt=np.genfromtxt('data/RT.txt', unpack=True)
x423,y423=np.genfromtxt('data/423K.txt', unpack=True)

#plt.plot(xrt[0:25]*((10)/(25)),generatediffernce(yrt),'x',color="orange")
#plt.plot(x423[0:25]*((10)/(25)),generatediffernce(y423),'x',color="blue")
plt.plot(xrt[0:25]*((10)/(25)),generatediffernce(yrt),label="Raumtemperatur",color="mediumblue")
plt.plot(x423[0:25]*((10)/(25)),generatediffernce(y423),label="423 Kelvin",color="m")
plt.plot(xrt[20]*((10)/(25)),generatediffernce(yrt)[20],'x',color="red")
plt.legend()
plt.grid()
plt.xlabel(r'$U_A/V$')
plt.ylabel(r'$I_A(U_A+\upDelta U_A)-I_A(U_A)$')
plt.yticks([])
plt.tight_layout()
plt.savefig('build/Differenz.pdf')
plt.figure()