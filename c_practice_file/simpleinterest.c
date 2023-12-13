// Value of Simple intrest;


#include<stdio.h>
int main()
{ 
float p ,r,t,x;
 printf(" Value of Simple intrest \n\n"); 
 printf(" Enter the value principle = "); 
 scanf("%f",&p);// input value ;
  printf(" Enter the value rate =  "); 
 scanf("%f",&r);// input value  ;
 printf(" Enter the value Time = "); 
 scanf("%f",&t);// input value;
 
 x= (p*r*t)/100;
  printf(" SI = \t %f\n",x);
 x = x+p;
 printf(" Total payable = %f\n",x);
}

