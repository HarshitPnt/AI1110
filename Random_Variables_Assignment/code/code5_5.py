import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1.9,0.1,19)
# print(x)

y=np.loadtxt('./prob.dat',dtype="double")
plt.plot(x,y,marker='o',mfc='r',label="Simulated")
plt.xlabel("$a$ (in B)")
plt.ylabel("$P_e$")
plt.title("$P_e$ v/s $a$")
plt.grid()
plt.legend()
plt.savefig("../../figures/plot_P.png")