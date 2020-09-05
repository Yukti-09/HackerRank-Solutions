#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    int d,rem=0;
    scanf("%d", &n);
    while(n!=0)
    {
        d=n%10;
        rem+=d;
        n=n/10;
    }
    printf("%d",rem);
    //Complete the code to calculate the sum of the five digits on n.
    return 0;
}

