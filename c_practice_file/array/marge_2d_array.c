#include<stdio.h>

    void main()
        {
            int a1[5],a2[5],a3[10],i,j;
            printf("enter 1st array\n");
            // input
             for(i=0;i<5;i++)
             {
             	printf("[%d] - ",i);
                scanf("%d",&a1[i]);
             }
              printf("enter 2nd array\n");
             for(i=0;i<5;i++)
             {
             	 printf("[%d] - ",i);
                scanf("%d",&a2[i]);
             }
             //  Marge logic
             int k=0;
        for(i=0;i<10;i++)
        {
            if(i>4)
            {
                a3[i]=a2[k];
                k++;
            }
            else
            {
                a3[i]=a1[i];
            }
        }
        printf("\n--------------------------\n");
    printf("\n Marge array \n");


        /// output 
    for(i=0;i<10;i++)
        {
            printf("[%d] - %d\n",i,a3[i]);
        }


////// shorting Accesding 
 int temp[10];
 
    for(i=0;i<10;i++) //8
        {
            for(j=0;j<=10;j++) //
                {
                    if(a3[j]>=a3[i])
                   {
                            temp[i]=a3[i];
                            a3[i]=a3[j];
                            a3[j]=temp[i];
                        }
                }
        }
    /// output shorting :-
    printf("\n--------------------------\n");
    printf("\n Shorting \n");

    for(i=0;i<10;i++)
    {
        printf("[%d] - %d\n",i,a3[i]);
    }
}
