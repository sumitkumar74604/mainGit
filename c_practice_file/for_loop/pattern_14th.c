/*	12345678
	 7654321
	  12345
	   4321
	    123
	     21
	      1
	      
*/






#include<stdio.h>
void main()
{
int i,j,k,l,y,m,x; 
printf(" enter digit you want to print loop \t");
//scanf("\n%d",&x);
for(i=1;i<=8;i++) // outer upper row loop
{
 for (j=1;j<=8;j++)  //   left side digit loop
  {
   printf("%d",j);
   y=j;
  }
  
  if(i==1)
  {
  for (j=y-1;j>=1;j--)  //   left side digit loop
  {
   printf("%d",j);
  }
 
  }
   printf("\n");
}


}
