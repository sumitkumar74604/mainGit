/////////////// switch case /////////


#include<stdio.h>
void main()
{
 int a ,temp, b,opt;
 printf(" \n **************wap to add ,sub,mul,divide with using switch case********* \n\n");
 printf(" enter value A = \t");
 scanf("%d",&a);
 printf(" enter value b = \t");
 scanf("%d",&b);

printf(" 1 to add \n");
printf(" 2 to sub \n");
printf(" 3 to multi \n");
printf(" 4 to divide \n");
printf(" 5 to mode remainder \n");
printf(" 6 to percentage \n"); 

printf("select operation \n");
scanf("%d",&opt);
switch (opt)
{
case 1:
 printf(" addition of  a ans b = %d \n",a+b);
break;

case 2:
 printf(" Subtract of  a ans b = %d \n",a-b);
break;

case 3:
 printf(" Multiplaction of  a ans b = %d \n",a*b);
break;

case 4:
 printf(" Divide of  a ans b = %d \n",a/b);
break;

case 5:
 printf(" divide's remainder of  a ans b = %d \n",a%b);
break;
case 6:
temp = (a*b)/100;
 printf(" percentage of  a ans b = %d \n",temp);
break;
default:
printf(" invalid\n");

}
 }
