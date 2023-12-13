/////////////////////// celsius / Fahrenheit//////////
#include<stdio.h>
int main()
{
printf("************ celsius / Fahrenheit ***********\n\n");

double fa,ce,ci,ft;
printf("enter celsius = \t");
scanf(" %lf",&ce);
printf("enter Fahrenheit = \t");
scanf(" %lf",&ft);
fa = ((ce*9)/5)+32;

printf(" Fahrenheit = %0.02f\n",fa);
ci = (ft-32)*5/9;
printf(" celsius = %0.02lf\n",ci);
}
