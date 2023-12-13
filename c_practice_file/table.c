//////////////// Table ///////////

#include<stdio.h>
void main()
{
int i=1,x , a,b,c;
printf("***************** Table ********\n\n ");
printf("enter the number\t ");
scanf("%d",&x);
while(i<=10)
{
c=x*i;
printf(" \n%d * %d = %d\n",x,i,c);
i++;
}
printf("\n");
}
