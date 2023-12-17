/* 	12345  *****
	1234-  ****
	123--  ***
	12---  **
	1----  *
	
	*/
	
	
#include<stdio.h>
void main()
{

int i,j,k,x;
printf(" enter pattern draw value \t");
scanf("%d",&x);
x=x+1;
for(i=1;i<=x;i++) // outer loop row 
 {
   
   for (j=1;j<=x-i;j++)
     // inner loop digit value
    {
      printf("%d",j);
    }
 printf("\n");
 }

}
