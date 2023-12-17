/* 	----*          1 
	---* *        2 3
	--* * *      4 5 6
	-* * * *    7 8 9 10
	* * * * *  11 12 13 14 
	
	
	*/
	
	
#include<stdio.h>
void main()
{
int i,j,k,count=0,x;
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
      count++;
        printf("%d_",count);     
    }
    
 printf("\n");
 }

}
