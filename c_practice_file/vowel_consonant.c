/////////////// switch case /////////


#include<stdio.h>
void main()
{
 
 char x;
 printf(" \n **************wap to vowel and consonant with using switch case********* \n\n");
 printf(" enter character  = \t");
 scanf("%c",&x);
switch (x)
{
case 'a':
case 'e':
case 'i':
case 'o':
case 'u':
case 'A':
case 'E':
case 'I':
case 'O':
case 'U':
printf("vowel\n");
break;
default:
if(x>=32&&x<=47||x>=58&&x<=64||x>=91&&x<=96||x>=123&&x<=127)
{
printf("special Character %c\n",x);
}
else
{
 if( x>=48&&x<=57)
 {
 printf(" Number %c \n",x);
}
else
printf(" consonant\n");
}
}
 }
