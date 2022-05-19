import numpy as np
from numpy import random as RN
N=10000000


#generating a sample space of size N
x1=RN.randint(1,N+1,size=N)
#if x belongs to {1,2,....,0.02*N} then he/she has cancer
x2=np.count_nonzero(x1<=.02*N)
#healthy
x3=N-x2

y1=RN.randint(1,N+1,size=N)
#if y belongs to {1,2,....,0.95*N} then positive test means he/she has cancer
y2=np.count_nonzero(y1<=.95*N)
y3=N-y2

y4=RN.randint(1,N+1,size=N)
#if y belongs to {1,2,.....,0.05*N} then negative test means he/she has cancer
y5=np.count_nonzero(y4<=.05*N)
y6=N-y5

print("Theoretical probability is ",(0.95*0.02)/(0.95*0.02+0.05*0.98))
print("Practical probability is ",((y2/N)*(x2/N))/((y2/N)*(x2/N)+(y3/N)*(x3/N)))