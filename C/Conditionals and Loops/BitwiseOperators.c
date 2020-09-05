#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k)
{
    int i;
    int j;
    int a[n];
    for(i=1;i<=n;i++)
    {
        a[i-1]=i;
    }
    int max=0;
    int max1=0;
    int max2=0;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(max<(a[i]&a[j]) && (a[i]&a[j])<k)
            max=a[i]&a[j];

            if(max1<(a[i]|a[j]) && (a[i]|a[j])<k) 
            max1=a[i]|a[j];

            if(max2<(a[i]^a[j]) && (a[i]^a[j])<k)
            max2=a[i]^a[j];
        }
    }
    printf("%d\n",max);
    printf("%d\n",max1);
    printf("%d\n",max2);

  
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
