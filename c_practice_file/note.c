#include<stdio.h>
int main()
{

 int x,y,z,m,n,o,p,q,r,s,t,u,v,w;
 printf("enter amount = ");
 scanf("%d",&x);
 y=x/2000;
 printf(" 2000 note = %d \n",y);
 z=x%2000;
 // printf(" 2000 r note = %d \n",z);
 m=z/1000;
 printf(" 1000 note = %d \n",m);
 n=z%1000;
  //printf(" 1000 r note = %d \n",n);
  o=n/500;
   printf(" 500 note = %d \n",o);
   p=n%500;
    //printf(" 500 r note = %d \n",p);
    q=p/100;
     printf(" 300  note = %d \n",q);
     r=p%100;
      //printf(" 300 r note = %d \n",r);
      s=r/50;
       printf(" 50  note = %d \n",s);
       t=r%50;
        //printf(" 50 r note = %d \n",t);
        u=t/20;
        printf(" 20 note = %d \n",u);
        v=t%20;
        //printf(" 20 r note = %d \n",v);
        w=v/10;
        printf(" 10 note = %d \n",w);
        y=v%10;
        //printf(" 10 r note = %d \n",y);
        z=y/5;
        printf(" 5 note = %d \n",z);
}
