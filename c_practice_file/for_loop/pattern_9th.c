/* 	----*          1 
	---* *        1 2
	--* * *      1 2 3
	-* * * *    1 2 3 4
	* * * * *  1 2 3 4 5 
	
	
	*/
	
	
#include<stdio.h>
void main()
{
int i,j,k,x;
printf(" enter pattern draw value \t");
scanf("%d",&x);
for(i=1;i<=x;i++) // outer loop row 
 {
   for(k=1;k<=x-i;k++) // space loop
   {
    printf("_");
    }
   for(j=1;j<=i;j++)  // inner loop digit value
    {
      printf("_%d",j);
      
    }
 printf("\n");
 }

}
