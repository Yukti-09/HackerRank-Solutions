#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    maxx=0
    a=''
    b=''
    st=set(s)
    l=list(st)
    for i in range(len(l)):
        for k in range(i+1,len(l)):
            a=l[i]
            b=l[k]
            x=str()
            flag=1
            for j in range(len(s)):
                if(s[j]==a or s[j]==b):
                    x+=s[j]
            for p in range(len(x)-1):
                if(x[p]==x[p+1]):
                    flag=0
            if(flag==1 and maxx<len(x)):
                maxx=len(x)
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
