////////// Alphabate ////////
#include<stdio.h>
void main()
{
int i,x;
for (i='A';i<='Z';i++)
{
printf("\t\t");
printf(" %c-",i);
printf("%d,\n",i);
x=i+32;
printf("%d-",x);
printf("%c",x);
}
printf("\n");
}
