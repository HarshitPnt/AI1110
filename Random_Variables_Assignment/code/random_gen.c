#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void genUniform(char *str, int len)
{
	FILE* fp;
	fp=fopen(str,"w");
	for(int i = 0; i <len;++i){
		double gen =(double) rand()/RAND_MAX;
		//printf("%lf",gen);
		fprintf(fp,"%lf\n",gen);
	}
	fclose(fp);
}

int main(){
	genUniform("uni.dat",1000000);
}
