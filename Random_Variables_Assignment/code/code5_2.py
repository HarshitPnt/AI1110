import numpy as np
import matplotlib.pyplot as plt 

y=np.loadtxt('max.dat',dtype="double")
x=np.linspace(0,1000000,1000000)
plt.scatter(x,y,label="noise")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of Y")
plt.savefig('../../figures/plot_Y.png')
