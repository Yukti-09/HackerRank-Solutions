#!/bin/python

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    max_count=0
    max_no=0
    count=0
    d={}
    for i in arr:
        if i not in d:
            d[i]=0
        d[i]+=1
    
    for i in d:
        if d[i]>max_count:
            max_no=i
            max_count=d[i]
    for i in arr:
        if i!=max_no:
            count+=1
    print(count)        
    return count                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = list(map(int, raw_input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
