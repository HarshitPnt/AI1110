import numpy as np
import matplotlib.pyplot as plt
import math

y=np.loadtxt('gau.dat',dtype='double')
x=np.linspace(-4,4,20)
cdf=[]
samples=1000000

for i in range(0,20):
    curr=np.size(np.nonzero(y<x[i]))/samples
    cdf.append(curr)

x_2=np.linspace(-4,4,10000)
cdf_the=[]
sum=0
y_2=[1/math.sqrt(2*math.pi)*math.exp((-i**2)/2) for i in x_2]
for i in range(0,9999):
    sum+=y_2[i]*(8/10000)
    cdf_the.append(sum)
plt.scatter(x,cdf,color="orange",label="Simulated")
plt.plot(x_2[:9999],cdf_the,label="Theoretical")
plt.grid()
plt.title("CDF")
plt.xlabel("x")
plt.ylabel("$F_X(x)$")
plt.legend()
plt.show()
