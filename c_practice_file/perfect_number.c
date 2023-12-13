#include<stdio.h>
int main()
{
int i,x,sum=0;
printf("*********** perfect number********\n\n");
printf("enter range \t");
scanf("%d",&x); //28
i=1;
while(i<x) //1<28 --true
{
 if(x%i==0)  
 {
   sum=sum+i; // 0+1
 }
 i++; 
}
if(sum==x)
 {
 printf(" number is perfect= %d\n",sum);
 }
 else
 printf(" this is not\n ");
}
