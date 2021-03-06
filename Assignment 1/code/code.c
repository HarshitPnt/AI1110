//code to verify the trigonometric idetity for a few values of theta

#include <stdio.h>
#include <math.h>

int main()
{
float x;//x to store sin(theta)
float y;//y to store cos(theta)
float z;//z to store tan(theta)
printf("Value of trigonometric expression at \ndifferent values of theta\n");
for(float i =0.3;i<2*M_PI;i=i+.3)
{	
	x = sin(i);
	y = cos(i);
	z = tan(i);
	float expression = (1+ (1/z) -(1/x))*(1+z+(1/y));
	printf("theta = %f , expression = %f\n",i,expression);
}
}
