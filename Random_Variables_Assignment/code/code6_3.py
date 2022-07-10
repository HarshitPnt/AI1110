import numpy as np 
import matplotlib.pyplot as plt
import mpmath as mp

samples=np.loadtxt("samp.dat",dtype="double")
x=np.linspace(0,2,30)
cdf_sim=[]
total=1000000

def pdf_the_gen(x):
    if(x<0):
        return 0
    else:
        return 0.5*mp.exp(-x/2)

for i in range(0,30):
    cdf_sim.append(np.size(np.nonzero(samples<x[i]))/total)

pdf_sim=[]

for i in range(0,29):
    pdf_sim.append((cdf_sim[i+1]-cdf_sim[i])/(x[i+1]-x[i]))

pdf_the=np.vectorize(pdf_the_gen,otypes=[np.float64])
plt.plot(x,pdf_the(x),color="orange",label="Theoretical")
plt.scatter(x[:29],pdf_sim,label="Simulated")
plt.xlabel('x')
plt.ylabel('$f_Y(y)$')
plt.title("PDF of Y")
plt.grid()
plt.legend()
plt.savefig('../../figures/PDF_6.png')