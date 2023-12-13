/////////////////////// ATM ///////////////////
#include<stdio.h>

void main()
{
 int deposite =1000 , withdrowal=0,with,input ,dep, pin=1234 ,quit ,p,a;
 char x,y,z,enter;
 a=deposite;
 printf("************** ATM *********** \n\n");
 printf("Enter your ATM Card and press y or Y \n");
 scanf("%c",&enter);
 if('y'==enter||'Y'==enter)
 {
 printf("Your is reeding please wait \n");
 printf(" please enter your security pin \n");
 scanf("%d",&p);
  if(p==pin )
  {
 printf(" 1. deposite \n");
 printf(" 2. withdrowal \n");
 printf(" 3. balance check \n");
 printf(" 4. quit \n");
  scanf("%d",&input);
   if(input==1)
   {
      printf(" enter your amount ");
      scanf("%d",&dep);
      printf(" your total deposite = %d\n",dep);
      deposite =deposite+dep;  
       printf(" your avilable balance is = %d\n ",deposite);
       
   }
   else
   {
      if(input==2)
      {
        printf("enter your amount = ");
        scanf("%d",&with);
        deposite = deposite - with;
        printf(" your withdrawal ammount is = %d\n",with);
        printf(" avilable balance is = %d\n",deposite);
      } 
      else
      {
        if(input==3)
        {
        printf(" your available balance = %d\n",a);
        }
       else  
       {
         if( input ==4)
         {
         printf(" thank you for visit here \n");
         }
       else   
      {
     printf(" invalid input\n");
      }
      }
   }
   }
   }
   if(p!=pin)
   {
    printf(" entered pin invalid \n");
   }
   }
 if(enter!='y'&&enter!='Y')
 {
   printf(" your transaction is failed please try again \n");
 }
}
