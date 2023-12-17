/*
	* - - - - -      *
	  *      ---   *
	*   *   --   *   *
	  *   * - *    * 
	*   *   *    *   *
	  *   *   *    *
	*   *        *   *
	  *            *
	*                *
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
  for(k=1;k<=x-i;k++) // space loop  
  {
   printf("  ");
  }
  for(l=1;l<=i;l++) //  right side digit loop
  {
    printf("%d",l);
  }
  printf("\n");
}

for(i=1;i<=x-1;i++) // lower loop
{
 for (j=1;j<=x-i;j++) // left side digit loop
  {
   printf("%d",j);
  }
  for(k=1;k<=i;k++) // space loop
  {
   printf("  ");
  }
  for(l=x-i;l>=1;l--) // right side digit loop
  {
   printf("%d",l);
  }
  printf("\n");
}

}
