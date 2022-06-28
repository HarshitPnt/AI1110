import numpy as np
import matplotlib.pyplot as plt

x_1=np.linspace(-0.5,1.5,20)
pr_sim=[]
pr_exp=[]
samples=1000000
y=np.loadtxt('uni.dat',dtype='double')
for i in range(0,20):
    pr_sim.append(np.size(np.nonzero(y<x_1[i]))/samples)



plt.scatter(x_1,pr_sim)
#plt.plot(x_1,pr_sim)
x=np.linspace(-1,2,10000)
y=[0 if x[i]<0 else x[i] if x[i]<1 else 1 for i in range(0,10000) ]
plt.plot(x,y,color="orange")
plt.grid()
plt.title("CDF")
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.savefig("./CDF.png")
