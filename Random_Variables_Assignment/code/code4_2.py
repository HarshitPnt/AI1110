import numpy as np
import matplotlib.pyplot as plt 

pr=[]
samples=np.loadtxt("tri.dat",dtype="double")
total=1000000
x=np.linspace(-4,4,20)
for i in range(0,20):
    pr.append(np.size(np.nonzero(samples<x[i]))/total)


plt.scatter(x,pr,label="Simulated")
plt.grid()

x_2=np.linspace(-4,4,1000)
pr_the=[0 if i<0 else (i**2)/2 if i<1 else (2-(2-i)**2)/2 if i<2 else 1 for i in x_2]
plt.plot(x_2,pr_the,color="orange",label="Theoretical")
plt.legend()
plt.ylabel("$F_T(t)$")
plt.title("CDF of Triangular Distribution")
plt.xlabel("t")
plt.savefig("../../figures/CDF_4")

