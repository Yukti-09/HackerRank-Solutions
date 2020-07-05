#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d={}
    ar=[]
    for i in arr:
        if i not in d:
            d[i]=0
        d[i]+=1
    max=0
    for i in d:
        if d[i]>max:
            max=d[i]
    for i in d:
        if d[i]==max:
            ar.append(i)
    print(min(ar))     
    return (min(ar))                  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
