////////////// Using while loop ./////////

#include<stdio.h>
void main()
{
int n, remain,rev=0,poly;
printf(" \n ************ reverse number **********\n\n");
printf("enter the number \t");
scanf("%d",&n); // input number 123
poly = n;

while(n!=0)
{
remain=n%10;  // 3
rev=(rev*10)+remain; //0*10+3=3 
n=n/10;  //12=123/10
}
printf("\n rev = %d\n",rev);
printf("\n after reversed check polynomial no.\n");
if(rev==poly)
{
printf("\n %d is polynomial \n",poly);
}
else
{
printf("\n %d is not polynomial \n",poly);
}
}
