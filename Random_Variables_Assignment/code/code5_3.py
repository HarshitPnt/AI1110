import numpy as np 
import matplotlib.pyplot as plt
import math
import mpmath as mp

pdf_sim=[]
samples=np.loadtxt("max.dat",dtype="double")
total=1000000
cdf_sim=[]
x=np.linspace(-10,10,100)
for i in range(0,100):
    cdf_sim.append(np.size(np.nonzero(samples<x[i]))/total)

# plt.scatter(x,pdf_sim)
for i in range(0,99):
    pdf_sim.append((cdf_sim[i+1]-cdf_sim[i])/(x[i+1]-x[i]))
plt.scatter(x[:99],pdf_sim,label="Simulated")
plt.grid()
plt.show()