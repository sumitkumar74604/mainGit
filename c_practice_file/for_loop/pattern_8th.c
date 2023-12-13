/* 	* * * * * 
	-* * * *
	--* * *
	---* * 
	----*  */
	
	
#include<stdio.h>
void main()
{
int i,j,k;
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

}
