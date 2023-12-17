#include<stdio.h>
#include<conio.h>
 void main()
 {
 	int i,a[5],b[5],c[5],sum=0,qty_sum=0;
 	for(i=1;i<=5;i++)
	 	{
		printf("enter product Qty. - [%d]\t",i);
	 	scanf("%d",&a[i]);
	 	printf("enter product price -[%d]\t",i);
	 	scanf("%d",&b[i]);
	 	printf("------------------------------\n");
		}
		
	for(i=1;i<=5;i++)
		{
			// Total Qty adding -------------
			 qty_sum=qty_sum+a[i];
			// Calculate Price logic 
			c[i]=a[i]*b[i];
			sum=sum+c[i];
			printf("\n[%d] Multiply =   %d * %d = %d",i,a[i],b[i],c[i]);
			printf("\tSUM = %d\n",sum);
		}
	printf("\nTotal SUM = %d\n",sum);
	printf("\nTotal Qty . = %d",qty_sum);
 
 }
