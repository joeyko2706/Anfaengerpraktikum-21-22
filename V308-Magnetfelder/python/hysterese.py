import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 


#Einfügen der Daten
B=np.array([3,104,276,394,475,531,576,610,642,668,696,682,667,648,626,600,566,523,460,342,131,-70,-147,-380,-472,-531,-578,-614,-646,-674,-700,-691,-676,-655,-632,-603,-570,-523,-457,-333,-123,78,267,400,485,544,589,625,655,684,715])
B2=np.array([0.003, 0.104, 0.276, 0.394, 0.475, 0.531, 0.576, 0.610, 0.642, 0.668, 0.696, 0.682, 0.667, 0.648, 0.626, 0.600, 0.566, 0.523, 0.460, 0.342, 0.131, -0.070, -0.147, -0.380, -0.472, -0.531, -0.578, -0.614, -0.646, -0.674, -0.700, -0.691, -0.676, -0.655, -0.632, -0.603, -0.570, -0.523, -0.457, -0.333, -0.123, 0.078, 0.267, 0.400, 0.485, 0.544, 0.589, 0.625, 0.655, 0.684, 0.715])
B3=B * 10^(-3)
I=np.array([0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0])

#magnetische Feldstärke der Spule nach Formel (5) bestimmen
my_0=4*np.pi*10**(-7)
n=595
r=0.135
H_Faktor=n*(2*np.pi*r)**(-1)
H_Spule=H_Faktor *I

B_Magnetisierung=(B*10**(-3)*(my_0)**(-1)-H_Spule)*my_0*10**3 
print(B_Magnetisierung)


#Remanenz:
plt.plot(H_Spule[20:21],B_Magnetisierung[20:21],'k*',label='Remanenz')
plt.plot(H_Spule[40:41],B_Magnetisierung[40:41],'k*')

#Sättigung
plt.plot(H_Spule[10:11],B_Magnetisierung[10:11],'m*',label='Sättigung')
plt.plot(H_Spule[30:31],B_Magnetisierung[30:31],'m*')

#Koerzitivkraft:
plt.plot(H_Spule[19:20],B_Magnetisierung[19:20],'y*',label='Koerzitivkraft')

#Neukurve:
plt.plot(H_Spule[0:10], B_Magnetisierung[0:10], 'b.', label = 'Neukurve')

#Kurvenverlauf 2:
plt.plot(H_Spule[10:30], B_Magnetisierung[10:30], 'g.', label = 'Kurve 2')

#Kurvenverlauf 3:
plt.plot(H_Spule[30:50], B_Magnetisierung[30:50], 'r.', label = 'Kurve 3')


plt.xlabel(r'$H\,/\,Am^{-1}$')
plt.ylabel(r'$B\,/\,$ mT')
plt.grid()
plt.legend()
plt.savefig("Hysteresekurve.pdf")