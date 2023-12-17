//// Wap to calculate gross salary and net salary . accept basic salary from user,TA ,i.e - 10% of basic salary , pf - 7.8% of basic salary , DA - 500 . PF ( gross salary = basic +DA+Ta ) and NS -  ( GS-PF )//////

// basic =100
// PF - (basic * 7.8)/100 = 7.80
// DA - 500
// TA - (Basic * 10)/100 = 10
#include<stdio.h>
int main()
{
 double basic,bs,gross,gs,ta,da=500,pf,ns;
 printf("\ngross salary and net salary \n\n");
 printf("Enter your Basic Salary :- \t");
 scanf("%lf",&basic);
 printf("Your Basic Salary  Account :- \t");
 printf("%0.02lf\n",basic);
 printf("\nYour PF Account :- \t");
 pf = (basic*7.8)/100;
 printf("PF = %0.02lf",pf);
 printf("\nYour TA account is :- \t");
 ta = (basic * 10)/100;
 printf("TA = %0.02lf\n",ta);
 printf("Your DA account is :- \t");
 printf("DA = %0.02lf\n",da);
 gross=basic+da+ta;
 printf("\nYour Gross salary :- %0.02lf \n\n",gross);
 ns=gross-pf;
 printf("\nyour Net Salary is :-  %0.02lf\n\n",ns); 

}
