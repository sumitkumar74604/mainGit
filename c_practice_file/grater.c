// Find the maximum value and print only A's value ;


#include<stdio.h>
int main()
{ 
int a,b,c,max;
 printf(" compare mamimum value of a \n\n"); 
 printf(" Enter a b = "); 
 scanf("%d%d",&a,&b);// input value ;
  scanf("%d",&b);
   //scanf("%d",&c);
   a=a+b;
   b=a-b;
   a=a-b;
   printf("swip a= %d b = %d \n", a,b);
 /*  max=(a+b+c);
   printf("Average of 3 no. = %d\n",max);
   max=max/3;
   printf("Average of 3 no. = %d\n",max);
 //(a>b&&b>c)?printf("a"):(b>c):printf("b"):printf("c");
//max=(a>b)?(b>c?a:c):(b>c?b:c);
//(a>=max)?printf("a\n"):printf("nul\n");*/
}

