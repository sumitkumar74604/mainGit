#include<stdio.h>
#include<conio.h>
  main()
 {
 	int a,b,x;
 	printf("enter value a - \t");
 	scanf("%d",&a);
 	printf("\nenter value b - \t");
 	scanf("%d",&b);
 	printf("\n 1. add ");
 	printf("\n 2. sub ");
 	printf("\n 3. Multi ");
 	printf("\n 4. Divide ");
printf("\nselect operation -");
scanf("%d",&x);
	switch(x)
	{
		case 1:printf("Add - %d",a+b);
		break;
		case 2:printf("Add - %d",a-b);
		break;
		case 3:printf("Add - %d",a*b);
		break;
		case 4:printf("Add - %d",a/b);
		break;
		default:
printf(" invalid\n");
	}
}
