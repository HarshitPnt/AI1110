#checking the result for 10 values of x from 1 to 10

for x in range(1,10000000):
	V_old=x**3
	x_new=0.99*x
	V_new=x_new**3
	v_percent=(V_old-V_new)/V_old*100
	print(v_percent)
