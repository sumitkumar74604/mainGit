	
#include<stdio.h>
void main()
{
int i,j,k;
for(i=1;i<=5;i++) // outer loop row 
 {
   for(k=1;k<=5-i;k++) // space loop
   {
    printf(" ");
    }
   for(j=1;j<=i;j++)  // inner loop digit value
    {
      printf("*");
      
    }
 printf("\n");
 }

}