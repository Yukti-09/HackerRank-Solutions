#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
   char s;
   char st[100];
   char str[100];
   scanf("%c",&s);
   scanf("%s",st);
   printf("%c\n",s);
   printf("%s\n",st);
   scanf(" %[^\t\n]s",str);
   printf("%s",str);
   return 0;
}

