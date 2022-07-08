#include "../func.h"

int main(){
    bernoulli("ber.dat",1,-1,0.5,1000000);
    max_like("ber.dat","../problem2/gau.dat","max.dat",0.5);
    printf("Pr(Y<0|X=1): %lf\n",max_error(1,"max.dat"));
    printf("Pr(Y>0|X=-1): %lf\n",max_error(-1,"max.dat"));
    maxProbError();
}  