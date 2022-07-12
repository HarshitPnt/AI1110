import numpy as np 
import mpmath as mp
import matplotlib.pyplot as plt
import math

def proberr_the_gen(x):
	return 1/2*(1-math.sqrt(x/(x+2)))

proberr_the = np.vectorize(proberr_the_gen, otypes=[np.float64])
y=np.loadtxt('err.dat',dtype="double")
x=np.linspace(1,10,10)
plt.semilogy(x,y,marker='o',color="red",label="Simulated")
x = np.linspace(1,10,1000)
plt.semilogy(x, proberr_the(x),color="blue",label="Theoretical")
plt.grid()
plt.xlabel("$\gamma$")
plt.ylabel("$P_e(\gamma)$")
plt.legend()
# plt.savefig('../../figures/plot_7_semilog.png')
plt.show()