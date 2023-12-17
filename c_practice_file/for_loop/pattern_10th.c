/* 	* * * * * 
	-* * * *
	--* * *
	---* * 
	----*  
	---* * 
	--* * * 
	-* * * *
                        * * * * *
                       		 */
#include<stdio.h>
void main()
{
int i,j,k,l,m;
for(i=1;i<=5;i++) // row
 {
 for(k=1;k<i;k++) // space loop
   {
    printf(" ");
   }
    for(j=5;j>=i;j--)  //collon
    {
      printf("* ");
    }
 printf("\n");
 }
 for(i=2;i<=5;i++) // outer loop row 
 {
   for(k=1;k<=5-i;k++) // space loop
   {
    printf(" ");
    }
   for(j=1;j<=i;j++)  // inner loop digit value
    {
      printf("%d ",j);
    }
 printf("\n");
 }
 }
