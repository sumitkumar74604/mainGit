





#include<stdio.h>
void main()
{
int i=1,x , a=0,b=1,c;
printf("***************** fibbnacci series ********\n\n ");
printf("enter the number ");
scanf("%d",&x);
while(i<=x)
{
c=a+b;
printf("\t a-%d+%d-b=%d-c ",a,b,c);
a=b;
printf(" \na value = %d",a);
b=c;
printf(" \nb value = %d",b);
i++;
}
printf("\n");
}
