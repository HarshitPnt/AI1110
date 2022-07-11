import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import math

def pdf_the_gen(x):
    return (mp.sqrt(3)/(mp.sqrt(2*math.pi)*100)*mp.exp(-((x-2000)**2)/(2*100*100/3)))

sample1=np.random.uniform(low=450,high=550,size=1000000)
sample2=np.random.uniform(low=450,high=550,size=1000000)
sample3=np.random.uniform(low=450,high=550,size=1000000)
sample4=np.random.uniform(low=450,high=550,size=1000000)

arr=np.array([sample1,sample2,sample3,sample4])
sample_final=arr.sum(axis=0)
cdf_the=[]

x=np.linspace(1800,2200,100)
for i in range(0,100):
    cdf_the.append(np.size(np.nonzero(sample_final<x[i]))/1000000)

pdf_sim=[]

for i in range(0,99):
    pdf_sim.append((cdf_the[i+1]-cdf_the[i])/(x[i+1]-x[i]))


pdf_the=np.vectorize(pdf_the_gen,otypes=[np.float64])
plt.plot(x,pdf_the(x),color="blue",label="Theoretical")
plt.ylabel("$f_R(r)$")
plt.xlabel("r")
plt.title("Plot of r and Gaussian Distribution")
plt.grid()
plt.scatter(x[:99],pdf_sim,color="orange",label="Simulated")
plt.legend()
plt.savefig('../../figures/PDF_assign8')