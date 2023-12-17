/////////////// Write a program that accepts four digits number from user and calculate the sum of first and last no./////////////

#include<stdio.h>
int main()
{
 int sum=0,x,a;
 printf("sum of first and last no.\n\n");
 printf(" enter the no. \t");
 scanf("%d",&x);
 while(x!=0)
 {
  a=x%10;
  sum=sum+a;
  x=x/10;
 } 
 printf("sum = %d\n\n",sum);

}
