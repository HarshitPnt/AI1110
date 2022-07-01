#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(){
	FILE* fp = fopen("gau.dat","r");
	double temp=0.0;
	double var=0.0;
	double current;
	while(fscanf(fp,"%lf",&current)!=-1){
		temp+=current;
		//printf("%lf",current);
		//printf("%lf",temp);
	}
	double mean = temp/1000000;
	fclose(fp);
	printf("%lf",mean);
	fp= fopen("gau.dat","r");
	temp =0.0;
	while(fscanf(fp,"%lf",&current)!=-1){
		current = pow(current-mean,2);
		temp+=current;
	}
	fclose(fp);
	printf("\n%lf\n",temp/1000000);
}
