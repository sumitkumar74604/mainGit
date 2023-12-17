#include<stdio.h>
void main()
{
 int x,y ;
 printf(" enter the year ");
 scanf("%d",&x);
 y=x%4;
 printf(" reaminder %d\n",y);
 if(x%4==0 && x%400==0)
 {
 printf(" leap year\n");
 }
 else
 printf("not\n");
 }
