import numpy as np
import matplotlib.pyplot as plt
import math

x=np.linspace(-4,4,20)
y=np.loadtxt('gau.dat',dtype='double')
pdf=[]
samples=1000000

for i in range(0,19):
 temp = ((np.size(np.nonzero(y<x[i+1]))-np.size(np.nonzero(y<x[i])))/(x[i+1]-x[i]))/samples
 pdf.append(temp)
plt.scatter(x[0:19],pdf,color='orange',label="Simulated")
x_2=np.linspace(-4,4,10000)
y_2=[1/math.sqrt(2*math.pi)*math.exp((-i**2)/2) for i in x_2]
plt.ylabel("$f_X(x)$")
plt.xlabel("x")

plt.title("PDF")
plt.plot(x_2,y_2,label="Theoretical")
plt.legend()
plt.grid()
plt.savefig("./PDF.png")