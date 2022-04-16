// code to verify the result for integral values of x from 1 to 10

#include <stdio.h>

int main()
{	
	double volume_old;
	double volume_new;
	double volume_percent;
	for(int x =1; x<=10;++x)
	{
		volume_old=x*x*x;
		double x_new=0.99*x;
		volume_new=x_new*x_new*x_new;
		volume_percent=(volume_old-volume_new)/volume_old*100;
		//printf("x is %d x_new is %lf v_old is %lf v_new is %lf\n",x,x_new,volume_old,volume_new);
		printf("%lf\n",volume_percent);
	}
	return 0;
}
