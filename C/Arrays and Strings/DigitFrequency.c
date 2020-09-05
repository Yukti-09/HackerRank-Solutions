#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char s[1000000];
    scanf("%s",s);
    int l=strlen(s);
    int j=0;
    int count=0;
    while(j<10)
    {
        count=0;
        for(int i=0;i<l;i++)
        {
            if((int)s[i]==48+j)
            count++;
        }
        printf("%d ",count);
        j++;
    }        

    return 0;
}
