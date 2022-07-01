import random
import numpy as np
import matplotlib.pyplot as plt
import math

x=np.loadtxt('../problem1/uni.dat',dtype="double")
x_2=np.log(1-x)
x_2=[i*(-2) for i in x_2]
#print(x_2)
x=np.linspace(-4,10,20)
cdf=[]
samples=1000000

for i in range(0,20):
    curr=np.size(np.nonzero(x_2<x[i]))/samples
    cdf.append(curr)

x_3=np.linspace(-4,10,1000)
y_3=[1-math.exp(-i/2) if i>0 else 0 for i in x_3 ]
plt.plot(x_3,y_3,label="Theoretical")
plt.scatter(x,cdf,label="Simulated",color="orange")
plt.xlabel("v")
plt.title("CDF")
plt.ylabel("$F_V(v)$")
plt.legend(loc='best')
plt.grid()
plt.savefig("./CDF.png")
