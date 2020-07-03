#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    inc=0
    dec=0
    mini=scores[0]
    maxi=scores[0]
    for i in range(1,len(scores)):
        if scores[i]>maxi:
            inc+=1
            maxi=scores[i]
        if scores[i]<mini:
            dec+=1
            mini=scores[i]
    return (inc,dec)            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
