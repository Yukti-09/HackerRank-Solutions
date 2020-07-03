#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    for i in range(len(s)-(m-1)):
        arr=[]
        summ=0
        for j in range(m):
            arr.append(s[i+j])
        for k in arr:
            summ+=k 
        if summ==d:
            count+=1
    print(count)
    return count    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
