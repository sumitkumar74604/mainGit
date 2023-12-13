////////////// Using while loop ./////////

#include<stdio.h>
void main()
{
int n,remain,rev=0,astro;
printf(" \n ************ Armstrong Number **********\n\n");
printf("enter the number \t");
scanf("%d",&n); // input number 123
astro = n;

while(n!=0)
{
remain=n%10;  // 3
rev=rev+remain*remain*remain;//27=0+3*3*3
n=n/10;  //12=123/10
}
printf("\n rev = %d\n",rev);
printf("\n after  check Armstrong Number no.\n");
if(rev==astro)
{
printf("\n %d is Armstrong Number no \n",astro);
}
else
{
printf("\n %d is not Armstrong Number no \n",astro);
}
}
