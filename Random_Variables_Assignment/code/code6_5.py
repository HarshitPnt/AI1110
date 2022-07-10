import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

def pdf_the_gen(x):
    return x*mp.exp(-(x**2)/2)

y=np.loadtxt('root.dat',dtype="double")

x=np.linspace(0,10,50)
cdf_sim=[]
for i in range(0,50):
    cdf_sim.append(np.size(np.nonzero(y<x[i]))/1000000)

pdf_sim=[]

for i in range(0,49):
    pdf_sim.append((cdf_sim[i+1]-cdf_sim[i])/(x[i+1]-x[i]))

plt.scatter(x[:49],pdf_sim,color="orange",label="Simulated")

pdf_the=np.vectorize(pdf_the_gen,otypes=[np.float64])

plt.plot(x,pdf_the(x),color="blue",label="Theoretical")
plt.grid()
plt.ylabel("$f_V(v)$")
plt.xlabel("v")
plt.legend()
plt.title("PDF of V")
plt.savefig("../../figures/PDF_6_2.png")
