#include<stdio.h>
#include<conio.h>
 void main()
 {
 	int a,b,c,max;
 	printf("enter value a - \t");
 	scanf("%d",&a);
 	printf("\nenter value b - \t");
 	scanf("%d",&b);
 	printf("\nenter value c - \t");
 	scanf("%d",&c);
 	// logic 1st -------------
 	
 	/**max=(a>b)?(a>c?a:c):(b>c?b:c);
 	printf("\nGrater is - %d",max);*/
 	
	 logic 2st -------------
	(a>b)&&(a>c)?printf("\na - %d",a):(b>c)?printf("\nb - %d",b):printf("\nc - %d",c);
 }
 
