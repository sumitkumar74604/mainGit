// sqare and cube;


#include<stdio.h>
int main()
{ 
float x,y,temp;
 printf(" sqare and cube \n\n"); 
 printf(" Enter the value square = "); 
 scanf("%f",&x);// input value ;
 printf(" Enter the value cube = "); 
 scanf("%f",&y);// input value ;
 
 x= x*x;
  printf(" square of given value is = %f \n",x); 
 y=y*y*y;
   printf(" cube of given value is = %f \n",y);
   temp=y-x;
     printf(" Difference of given value cube and square is  = %f\n",temp);
}

