///////////// Positive value ///////////

#include<stdio.h>

void main()
{
 int z,y,a,b;
 float x;
  printf(" Check value Round up \n");
  printf("enter your value\n ");
   scanf("%f",&x);
  
    if(x>0);
     {
       y=x*10;
       z=y%10;
       if(z>=5)
       {
        a=x;
        a++;
       }
     else
     {
     a=x;
      }
    printf(" %d \n",a);
}
/*else if(x<0)
     {
     x=-(x);
       y=x*10;
       z=y%10;
       if(z>=50)
       {
        a=x;
        a--;
       }
     else
     
     {
     a=x;
      }
    printf(" %d \n",a);
}*/
 if(x==0)
{
printf(" given value is zero\n");
}
}
