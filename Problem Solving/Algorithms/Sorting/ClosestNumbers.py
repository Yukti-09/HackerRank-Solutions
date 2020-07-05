#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    l=[]
    small=abs(arr[0]-arr[1])
    for i in range(1,len(arr)):
        if abs(arr[i-1]-arr[i])<small:
            small=abs(arr[i-1]-arr[i])
    for i in range(1,len(arr)):
            if abs(arr[i-1]-arr[i])==small:    
                print(arr[i-1],end=" ")
                print(arr[i],end=" ")
                l.append(arr[i-1])
                l.append(arr[i])
    return l            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
