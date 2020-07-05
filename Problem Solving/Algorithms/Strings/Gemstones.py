#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    l=[]
    for i in arr:
        l.append(set(i))
    l1=list(max(l))
    count1=0
    count=0
    for i in l1:
        count1=0
        for j in l:
            if i in j:
                count1+=1
        if(count1==len(l)):
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
