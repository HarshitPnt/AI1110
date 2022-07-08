import numpy as np 
import matplotlib.pyplot as plt
import math
import mpmath as mp

cdf_sim=[]
samples=np.loadtxt("max.dat",dtype="double")
total=1000000
x=np.linspace(-10,10,1000)
for i in range(0,1000):
    cdf_sim.append(np.size(np.nonzero(samples<x[i]))/total)


plt.scatter(x,cdf_sim,label="Simulated")
plt.grid()
plt.show()