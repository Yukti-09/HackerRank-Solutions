#!/bin/python3

import math
import os
import random
import re
import sys
width=[]

# Complete the serviceLane function below.
def serviceLane(n, cases):
    l=[]
    for i in range(len(cases)):
        arr=[]
        for j in range(cases[i][0],cases[i][1]+1):
            arr.append(width[j])
        l.append(min(arr))
    print(min(arr))
    return l
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
