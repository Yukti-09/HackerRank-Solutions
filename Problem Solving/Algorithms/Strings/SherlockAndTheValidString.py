#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d={}
    for i in s:
        if i not in d:
            d[i]=0
        d[i]+=1    
    count=0
    l=list(d.values())
    c=l[0]
    for i in d:
        if d[i]==c:
            count+=1
    if count==len(l) or count==len(l)-1:
        print("YES")
        return "YES"
    else:
        print("NO")
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
