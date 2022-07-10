#include "../func.h"

int main(){
    chi("gau1.dat","gau2.dat","samp.dat",1000000);
    gen_root("samp.dat","root.dat");
}