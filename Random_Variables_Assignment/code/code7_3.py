import numpy as np 
import mpmath as mp
import matplotlib.pyplot as plt
import math

def proberr2(x):
	return 1/2*(1-math.sqrt(x/(x+2)))

expected_err_vec = np.vectorize(proberr2, otypes=[np.float64])
y=np.loadtxt('err.dat',dtype="double")
x=np.linspace(1,10,10)
plt.semilogy(x,y,marker='o',color="red",label="Simulated")
x = np.linspace(1,10,1000)
plt.semilogy(x, expected_err_vec(x),color="blue",label="Theoretical")
plt.grid()
plt.xlabel("$\gamma$")
plt.ylabel("$P_e(\gamma)$")
plt.legend()
# plt.savefig('../../figures/plot_7_semilog.png')
plt.show()
