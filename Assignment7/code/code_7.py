import matplotlib.pyplot as plt
import numpy as np
import math

def gen1(x):
    value = 1/((2*math.pi)**0.5)*np.exp((-x**2)/2)
    return value

xlist = np.linspace(-10,10,num=1000)
ylist=gen1(xlist)
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist,label='N(0,1)')
plt.grid()
plt.title('Gaussian Distribution Of X')
plt.xlabel('x')
plt.ylabel('$f_X(x)$')
plt.legend(loc='best')
plt.savefig('fig/1.png')
plt.clf()

def gen2(x):
    Y=1/((2*math.pi*x)**0.5)*np.exp(-x/2)
    return Y

xlist=np.linspace(0.1,10,1000)
ylist=gen2(xlist)
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist,label="$f_Y(y)$")
plt.grid()
plt.legend()
plt.title('PDF of Y')
plt.xlabel('y')
plt.ylabel('$f_Y(y)$')
plt.savefig('fig/2.png')
plt.clf()

def gen3(x):
    if(abs(x)<=1):
        return 1/2
    else:
        return 0

xlist=np.linspace(-2,2,1000)
ylist=[]
for i in range(len(xlist)):
    ylist.append(gen3(xlist[i]))
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist,label="$f_X(x)$")
plt.grid()
plt.legend()
plt.title('PDF of X')
plt.xlabel('x')
plt.ylabel('$f_X(x)$')
plt.savefig('fig/3.png')
plt.clf()

def gen4(x):
    if(abs(x)<=1):
        return 0.5+x/2
    elif x>1:
        return 1
    else:
        return 0

xlist=np.linspace(-2,2,1000)
ylist=[]
for i in range(len(xlist)):
    ylist.append(gen4(xlist[i]))
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist,label="$F_X(x)$")
plt.grid()
plt.legend()
plt.title('CDF of X')
plt.xlabel('x')
plt.ylabel('$F_X(x)$')
plt.savefig('fig/4.png')
plt.clf()

def gen5(x):
    if(x<=1 and x>0):
        return 1/(2*(x**0.5))
    else:
        return 0

xlist=np.linspace(-2,2,1000)
ylist=[]
for i in range(len(xlist)):
    ylist.append(gen5(xlist[i]))
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist,label="$f_Y(y)$")
plt.grid()
plt.legend()
plt.title('PDF of Y')
plt.xlabel('y')
plt.ylabel('$f_Y(y)$')
plt.savefig('fig/5.png')
plt.clf()

def gen(x,k):
    if(x>0):
        return 1/((2**(k/2)*math.gamma(k/2)))*(x**(k/2-1))*math.exp(-x/2)
    else:
        return 0

ax = plt.gca()
ax.set_xlim([0.05, 0.5])
ax.set_ylim([0, 1])
plt.axis([-0.05,0.5,0,1])
xlist=np.linspace(-0.05,10,1000)
plt.figure(num=0,dpi=120)
ylist1=[]
for i in range(len(xlist)):
    ylist1.append(gen(xlist[i],2))
plt.plot(xlist,ylist1,label='n=2')
ylist2=[]
for i in range(len(xlist)):
    ylist2.append(gen(xlist[i],3))
plt.plot(xlist,ylist2,label='n=3')
ylist3=[]
for i in range(len(xlist)):
    ylist3.append(gen(xlist[i],4))
plt.plot(xlist,ylist3,label='n=4')
ylist=[]
for i in range(len(xlist)):
    ylist.append(gen(xlist[i],5))

plt.plot(xlist,ylist,label="n=5")
plt.grid()
plt.legend()
plt.title('PDF of Chi-squared Distribution')
plt.xlabel('y')
plt.ylabel('$f_Y(y)$')
plt.savefig('fig/6.png')
plt.clf()