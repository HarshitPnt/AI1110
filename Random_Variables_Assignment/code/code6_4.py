import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

def cdf_the_gen(x):
    return 1-mp.exp(-x**2/2)

y=np.loadtxt('root.dat',dtype="double")

x=np.linspace(0,10,50)
cdf_sim=[]
for i in range(0,50):
    cdf_sim.append(np.size(np.nonzero(y<x[i]))/1000000)

plt.scatter(x,cdf_sim,color="orange",label="Simulated")

cdf_the=np.vectorize(cdf_the_gen,otypes=[np.float64])
plt.plot(x,cdf_the(x),color="blue",label="Theoretical")

plt.legend()
plt.ylabel("$F_v(v)$")
plt.xlabel("v")
plt.grid()
plt.savefig('../../figures/CDF_6_2.png')

