import numpy as np

for i in range(1,20):
    	
	#input parameter
    
	x=i*0.3
	y = (1+1/np.tan(x)-1/np.sin(x))*(1+np.tan(x)+1/np.cos(x))
        
       #output
       
	print(y)
