#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    l=[]
    i=0
    while(arr):
        count=0
        mini=arr[0]
        for i in range(len(arr)):
            if(arr[i]==mini):
                count+=1
            else:
                break
        for j in range(count):
            arr.remove(arr[0])
        for i in range(len(arr)):
            arr[i]-=mini
            count+=1
        l.append(count)
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
