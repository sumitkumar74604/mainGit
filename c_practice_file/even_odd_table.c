////////// even or odd ////////
#include<stdio.h>
void main()
{
int i,x,sum=0,osum=0;
printf(" enter the value to find even or odd\t");
scanf("%d",&x);
for (i=1;i<=x;i++)
{

if(i%2==0)
{
printf(" even =  %d \n",i);
sum=sum+i;
}
else
{
printf("\t");
printf(" odd = %d",i);
osum = osum+i;
}
}
printf("\nodd sum = %d ",osum);
printf("even sum = %d\n ",sum);
printf("\n");

}
