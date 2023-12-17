/*
	* - - - - 1
	* * - - - 12   
	* * * - - 123
	* * * * - 1234
	* * * * * 12345
	* * * * - 1234
	* * * - - 123
	* * - - - 12    
	* - - - - 1      
*/

#include<stdio.h>
void main()
{
int i,j,k,l,m,x; 
printf(" enter digit you want to print loop \t");
scanf("\n%d",&x);
for(i=1;i<=x;i++) // outer upper row loop
{
 for (j=1;j<=i;j++)  //   left side digit loop
  {
   printf("%d",j);
  }
  printf("\n");
}
for(i=1;i<x;i++) // lower loop
{
 for (j=1;j<=x-i;j++) // left side digit loop
  {
   printf("%d",j);
  }
  printf("\n");
}
}
