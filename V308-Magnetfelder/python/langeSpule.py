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

#B, x = np.genfromtxt("LangeSPule.txt", unpack = True)

B = np.array([2.230, 2.150, 1.981, 1.623, 1.053, 0.562, 0.307, 0.177, 0.110, 0.075])
x = np.array([86, 96, 106, 116, 126, 136, 146, 156, 166, 176])


plt.xlabel(r'Abstand $x$ / mm')
plt.ylabel(r'$B$ / mT')
plt.plot(x, B, 'b.',label= 'Messerte')
plt.legend()
plt.savefig('langeSpule.pdf')


