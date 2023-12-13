/////////////// Wap to to check calculate area of different shap based on user choice s,c,or r ( like square, circleand rectangle /////////


#include<stdio.h>
void main()
{
 int x;
 double circle,squre,rectangle,r,pi=3.14,l,b;
 printf(" \n ************** square, circleand rectangle ********* \n\n");

printf(" 1 to circle \n");
printf(" 2 to rectangle \n");
printf(" 3 to square \n");

printf("select operation \n");
scanf("%d",&x);
switch (x)
{
case 1:
 printf("Area of circle \n");
 printf("enter the radious \t");
scanf("%lf",&r);
circle=pi*r*r;
printf(" circle = %0.02lf\n",circle);
break;

case 2:
 printf(" Area or rectangle \n");
 printf(" enter length \t");
 scanf("%lf",&l);
 printf(" \nenter width\t");
 scanf("%lf",&b);
 printf(" \n area of rectangle of %0.02lf and %0.02lf = %0.02lf \n\n",l,b,l*b); 
break;

case 3:
 printf(" Area or Square \n");
 printf(" enter length \t");
 scanf("%lf",&l);
 printf(" \narea of square of %0.01lf = %0.02lf \n",l,l*l);
break;


default:
printf(" this is invalid please select valid option \n");

}
 }
