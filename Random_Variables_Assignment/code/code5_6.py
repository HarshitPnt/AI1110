import numpy as np 
import matplotlib.pyplot as plt
import matplotlib
import math
import mpmath as mp


def q_func(x):
    return(mp.erfc(x/math.sqrt(2))/2)

x=np.linspace(1.9,0.2,19)


y=np.loadtxt('./prob.dat',dtype="double")

# ax.plot(x,y,color="orange",marker='o')
# ax.set_yscale("log")
plt.semilogy(x,y,marker='o',mfc='r',label="Simulated")
plt.xlabel("$a$ (in B)")
plt.ylabel("$P_e$")
plt.title("$P_e$ v/s $a$")
plot_the=np.vectorize(q_func,otypes=[np.float64])
plt.grid()
x_2=np.linspace(0,5,40)
plt.semilogy(x_2,plot_the(x_2),color="blue",label="Theoretical")
plt.legend()
plt.savefig('../../figures/semilog_5.png')