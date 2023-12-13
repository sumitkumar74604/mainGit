 ////////// Alphabate print 5th position////////
#include<stdio.h>
void main()
{
int i;
char d;

for (i='A';i<='Z';i++)
{
printf("\t\t");
printf(" %c-",i);
printf("%d,\t",i);
}
printf("\n\n After find 5th accouding to no.\n\n\n");


for (i='A';i<='Z';i++)
{
printf("\t\t");
printf(" %c-",i);
printf("%d,\n",i);
i=(i+4);
}

printf("\n\n After find 5th position accouding to Alphabet\n");
for(i='A';i<'Z';i++)
{
/*printf(" \t%c-",c-1);
printf("%d,\n",i-1);*/
i=(i+4);
d=i;
printf("\t%d-",d);
printf("%c\n",d);
}
printf("\n\n\n\n");



for (i='a';i<='z';i++)
{
printf("\t\t");
printf(" %c-",i);
printf("%d,",i);
}
printf("\n\n After find 5th accouding to no.\n\n  \n");
for (i='a';i<='z';i++)
{
printf("\t\t");
printf(" %c-",i);
printf("%d,\n",i);
i=(i+4);
}


printf("\n\n After find 5th position accouding to Alphabet\n");
for(i='a';i<'z';i++)
{
/*printf(" \t\t%c-",c-1);
printf("%d,\n",i-1);*/
i=(i+4);
d=i;
printf("\t%d-",d);
printf("%c\n",d);
}
printf("\n");
}
