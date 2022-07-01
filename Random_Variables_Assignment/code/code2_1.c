#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void gaussian(char *str,int len){
	FILE* fp = fopen(str,"w");
	for(int i = 0;i<len;++i)
	{
		double curr=0;
		for(int j = 0;j<12;++j){
			double uni= (double)rand()/RAND_MAX;
			curr+=uni;
		}
		curr-=6;
		fprintf(fp,"%lf\n",curr);
	}
	
}

int main(){
	gaussian("gau.dat",1000000);
}

