#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    p=0
    q=0
    for i in range(n):
        for j in range(n):
            if(i==j):
                p+=arr[i][j]
            if((i+j)==n-1):
                q+=arr[i][j]
    if(p>q):
        return p-q
    else:
        return q-p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
