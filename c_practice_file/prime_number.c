////////////// Prime no./////////
#include<stdio.h>
int main()
{
int i,j,x,count=0;
printf("************* prime no.**********\n\n");
printf("enter range");
scanf("%d",&x); // range 20


for(i=2;i<=x;i++) // 4<=20?  
{
  for(j=2;j<=i;j++) // 3<=4?
  {
    if(i%j==0) // 2%2=0
    {
      break;
    }
  }
  if(i==j) //2=2?
  {
   printf("  prime no %d\n",i);
  }
 /* else 
  {
  printf(" \t");
  printf(" not prime %d",i);
  
  }*/
}
for(i=2;i<=x/2;i++)

{
if(x%i==0)

{
 count++;
}
}
if(count==0){
printf("%d prime\n",x);}
else{
printf(" %d is not prime\n ",x);
}
}
