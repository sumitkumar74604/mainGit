/*
	abcde
	abcd
	abc
	ab
	a
*/
#include<stdio.h>
void main()
{
int i,j;


for(i=1;i<=26;i++) // lower loop
{
 for (j=65;j<=91-i;j++) // left side digit loop
  {
   printf("%c ",j);
  }
  printf("\n");
}
for(i='a';i<='z';i++) // lower loop
{
 for (j='z';j>=i;j--) // left side digit loop
  {
   printf("%c ",j);
  }
  printf("\n");
}
}

