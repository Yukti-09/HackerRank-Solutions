#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    for num in range(i,j+1):
        copy=num
        rev=0
        while copy!=0:
            rev=(rev*10)+copy%10
            copy=copy//10
        if (abs(rev-num))%k==0:
            count+=1
    print(count)   
    return count     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
