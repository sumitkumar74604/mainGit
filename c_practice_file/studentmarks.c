// student marks and %;


#include<stdio.h>
int main()
{ 
float math,english,hindi,sci, sst,x,y;
 printf(" student marks and and percentage \n\n"); 
 printf(" Enter the value math = "); 
 scanf("%f",&math);// input value math ;
  printf(" Enter the value english =  "); 
 scanf("%f",&english);// input value english ;
 printf(" Enter the value hindi = "); 
 scanf("%f",&hindi);// input value hindi ;
  printf(" Enter the value science =  "); 
 scanf("%f",&sci);// input value science ;
 printf(" Enter the value sst = "); 
 scanf("%f",&sst);// input value sst ;
 
 x= (math+english+hindi+sci+sst);
 printf(" \n total marks = %f\n",x);
 
 y=(x*100)/500;
 printf(" \n total percentage = %f \n",y); 
}

