import numpy as np 
import matplotlib.pyplot as plt 

pr=[]
samples=np.loadtxt("tri.dat",dtype="double")
total=1000000
x=np.linspace(-1,3,40)
for i in range(0,40):
    pr.append(np.size(np.nonzero(samples<x[i]))/total)

# plt.scatter(x,pr)

pdf_sim=[]
for i in range(0,39):
    pdf_sim.append((pr[i+1]-pr[i])/(x[i+1]-x[i]))
plt.scatter(x[:39],pdf_sim,label="Simulated")
x=np.linspace(-1,3,10000)
pdf_the=[0 if i<0 else i if i<1 else 2-i if i<2 else 0 for i in x]

plt.plot(x,pdf_the,color="orange",label="Theoretical")
plt.legend()
plt.ylabel("$f_T(t)$")
plt.xlabel("t")
plt.title("PDF of Trianggular Distribution")
plt.grid()
plt.savefig("../../figures/PDF_4.png")