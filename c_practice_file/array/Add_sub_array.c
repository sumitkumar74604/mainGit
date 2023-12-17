#include<stdio.h>
void main()
{ 
 int a[5],b[5],c[5],d[5],e[5],f[5],g[5],i;
 
 
 for(i=0;i<5;i++)
 {
 printf("%d enter the value a = \t",i);
 scanf("%d",&a[i]); 
 printf("%d enter value b = \t",i);
 scanf("%d",&b[i]); 
 }
 for(i=0;i<5;i++)
 {
 c[i]=a[i]+b[i];
 d[i]=a[i]-b[i];
 e[i]=a[i]*b[i];
 f[i]=a[i]/b[i];
 g[i]=a[i]%b[i];
 }
 printf("\n your input value is \n");
 for(i=0;i<5;i++)
 {
  printf("  \n %d - %d + %d = %d  ",i,a[i],b[i],c[i]);
  printf("  \n %d - %d - %d = %d  ",i,a[i],b[i],d[i]);
  printf("  \n %d - %d * %d = %d  ",i,a[i],b[i],e[i]);
 printf("  \n %d - %d / %d = %d  ",i,a[i],b[i],f[i]);
  printf("  \n %d - %d mode %d = %d  ",i,a[i],b[i],g[i]);
  //printf("  \n %d add = %d  ",a,d[i]);
 }
 
printf("\n");
 
}


