#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

//Function to generate a sample of size <len> for a Uniform Random variable and storing it in a file of name <str>
void genUniform(char *str, int len)
{
	FILE* fp;
	fp=fopen(str,"w");
	srand(time(0));
	for(int i = 0; i <len;++i){
		double gen =(double) rand()/RAND_MAX;
		//printf("%lf",gen);
		fprintf(fp,"%lf\n",gen);
	}
	fclose(fp);
}

//function to calculate the mean of the sample of size <len> stored in file <str> 
double myMean(char *str,int len){
    FILE* fp = fopen(str,"r");
	double temp=0.0;
	double var=0.0;
	double current;
	while(fscanf(fp,"%lf",&current)!=-1){
		temp+=current;
	}
	double mean = temp/len;
	fclose(fp);
    return mean;
}

//function to calculate the variance of the sample of size <len> stored in file <str> 
 double myVariance(char *str,int len){
    FILE* fp;
    fp= fopen(str,"r");
	double var =0.0;
    double current=0.0;
    double avg=myMean(str,len);
	while(fscanf(fp,"%lf",&current)!=-1){
		current = pow(current-avg,2);
		var+=current;
	}
	fclose(fp);
	return (var/len);
 }

void gaussian(char *str,int len,int uni_num){
	FILE* fp = fopen(str,"w");
	srand(time(0));
	for(int i = 0;i<len;++i)
	{
		double curr=0;
		for(int j = 0;j<uni_num;++j){
			double uni= (double)rand()/RAND_MAX;
			curr+=uni;
		}
		curr=pow(12,0.5)*(curr-uni_num/2)/pow(uni_num,0.5);
		fprintf(fp,"%lf\n",curr);
	}
	
}

void genTriangular(char * str1, char* str2, char *str3, int len){
	genUniform(str1,len);
	sleep(1);
	genUniform(str2,len);
	FILE* fp1=fopen(str1,"r");
	double var1;
	FILE* fp2= fopen(str2,"r");
	double var2;
	FILE* fp3 =fopen(str3,"w");
	while(fscanf(fp1,"%lf",&var1)!=-1){
		fscanf(fp2,"%lf",&var2);
		fprintf(fp3,"%lf\n",var1+var2);
	}
	fclose(fp1);
	fclose(fp2);
	fclose(fp3);
	}


void bernoulli(char *str, int a, int b, double p,int len){
	srand(time(0));
	
	FILE* fp=fopen(str,"w");
	for (int i = 0;i<len;++i){
		double temp=(double)rand()/RAND_MAX;
	
		if(temp<=p){
			
			fprintf(fp,"%d\n",a);
		}
		else{
		
			fprintf(fp,"%d\n",b);
		}
	}
	fclose(fp);
}

void max_like(char* ber,char* gau,char* out,double a){
	FILE* fp1=fopen(ber,"r");
	FILE* fp2=fopen(gau,"r");
	FILE* fp3=fopen(out,"w");
	double var1,var2;
	while(fscanf(fp1,"%lf",&var1)!=-1){
		fscanf(fp2,"%lf",&var2);
		fprintf(fp3,"%lf\n",(a*var1+var2));
	}
	fclose(fp1);
	fclose(fp2);
	fclose(fp3);
}

double max_error(int mode,char* str){
	FILE* fp1=fopen(str,"r");
	FILE* fp2=fopen("ber.dat","r");
	int count_fav=0 ,count_total_1=0,count_total_2=0;
	double var1,var2;
	while(fscanf(fp1,"%lf",&var1)!=-1){
		fscanf(fp2,"%lf",&var2);
		if(var2==1)
			count_total_1++;
		else
			count_total_2++;
		
		if(mode==1&&var1<0&&var2==1){
			++count_fav;
		}
		else if(mode==-1&&var2==-1&&var1>0){
			++count_fav;
		}
		}
	return mode==1?((double)(count_fav)/count_total_1):((double)(count_fav)/count_total_2);
}

void maxProbError(){
  for(double i=0.1;i<=2.0;){
    max_like("ber.dat","../problem2/gau.dat","./Data/max.dat",i);
    FILE* fp=fopen("prob.dat","a");
    double var1=max_error(1,"./Data/max.dat");
    double var2=max_error(-1,"./Data/max.dat");
    fprintf(fp,"%lf\n",(var1+var2)/2);
    i+=0.1;
  }
}

void chi(char *str1, char *str2,char *str3,int len){
	gaussian("gau1.dat",len,36);
    sleep(1);
    gaussian("gau2.dat",len,36);
    FILE* fp1 =fopen(str1,"r");
    FILE* fp2 =fopen(str2,"r");
    FILE* fp3 =fopen(str3,"w");

    double var1;
    double var2;
    double var3;
    while(fscanf(fp1,"%lf",&var1)!=-1){
        fscanf(fp2,"%lf",&var2);
        var3=pow(var1,2)+ pow(var2,2);
        fprintf(fp3,"%lf\n",var3);
        }
        fclose(fp1);
        fclose(fp3);
        fclose(fp2);
}

void gen_root(char *str,char *str2){
	FILE* fp =fopen(str,"r");
	FILE* fp2=fopen(str2,"w");
	double var;
	while(fscanf(fp,"%lf",&var)!=-1){
		fprintf(fp2,"%lf\n",pow(var,0.5));
		// printf("%lf\n",var);
	}
	fclose(fp);
	fclose(fp2);
}

double myGauss(){
	double temp=0;
			for(int k=0;k<12;++k){
				temp+=(double)rand()/RAND_MAX;
			}
			temp-=6;
	return temp;
}





void myChi(char* str,int num, int len){
	FILE* fp=fopen(str,"w");

	for(int i = 0; i< len;++i){
		double chi=0;
		for (int j =0;j<num;++j){
			double temp=myGauss();
			chi+=temp*temp;
			
		}
		fprintf(fp,"%lf\n",chi);
	}
	fclose(fp);
}



void gen_rayl(char *str,  double gamma,int num){
  FILE *fp=fopen(str,"w") , *fp2 = fopen("ber.dat","r");
  double bern = 0;
  while(fscanf(fp2,"%lf",&bern)!=-1){
    double sig = gamma/2;
	double a=0;
	double sum=0;
	for(int i =0 ;i < num;++i){
		a = myGauss()*sqrt(sig);
		sum+=a*a;
	}
	 double final = bern*sqrt(sum) + myGauss();

    fprintf(fp, "%lf\n", final);
  }
  fclose(fp);
  return;
}

void prob_err(char* str , double a){
  FILE *fp, *fp2 = fopen(str, "w");
  double temp;
  for(int i=1;i<=10; i++){
    gen_rayl("cond_prob.dat", a*i,2);
    temp = max_error(1,"cond_prob.dat");
    fprintf(fp2,"%lf\n",temp);
  }

  fclose(fp2);
  return;
}