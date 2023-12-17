////////// factorial //////////

#include<stdio.h>
int main()
{
int i=1,x,fact=1;
printf("enter the number ");
scanf("%d",&x);
while(i<=x)
{
fact=fact*i;
i++;
}
printf("fact %d \n",fact);
/*

for(i=1;i<=x;i++)
{
fact = fact*i;
}
printf("%d fact = %d\n",x,fact);

}*/
}
