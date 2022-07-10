import numpy as np 
import matplotlib.pyplot as plt 
import math
import mpmath as mp

samples=np.loadtxt("samp.dat",dtype="double")
x=np.linspace(-2,2,40)
cdf_sim=[]
total=1000000

def 

for i in range(0,40):
    cdf_sim.append(np.size(np.nonzero(samples<x[i]))/total)

plt.scatter(x,cdf_sim,label="Simulated")
plt.grid()

# def q_func(i):
#     return (1-mp.erf(i))/2

def cdf_the_gen(x):
    if(x<=0):
        return 0
    else:
        return 1-mp.exp(-x/2)


# def erf(i):
#     x=np.linspace(0,i,10000)
#     y=[math.exp((-(a)**2)) for a in x]
#     sum=0
#     for b in y:
#         sum+=b*0.0001
#     return 2*sum/math.sqrt(math.pi)


# def cdf_the(t):
#     x=np.linspace(-1,1,1000)
#     y=[1/1/((2*math.pi)**0.5)*(math.exp(-(i**2)/2))*erf(math.sqrt((t-i**2)/2))/500 if (t-i**2)>0 else 0.0 for i in x]
#     sum=0
#     for i in y:
#         sum+=i
#     #y=[1/((2*math.pi)**0.5)*(math.exp)**(-(i**2)/2)*erf(math.sqrt((t-i**2)/2))/50 for i in x]
#     return sum

x=np.linspace(-2,2,100)
# cdf_theoretical=[cdf_the(t) for t in x]
# plt.plot(x,cdf_theoretical)

cdf_the=np.vectorize(cdf_the_gen,otypes=[np.float64])
plt.plot(x,cdf_the(x),color="orange",label="Theoretical")
plt.legend()
plt.savefig('../../figures/CDF_6.png')