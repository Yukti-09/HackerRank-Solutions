#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    l=len(arr)
    arr=sorted(arr)
    sum1=0
    sum2=0
    for i in range(0,l-1):
        sum1+=arr[i]    
    for j in range(1,l):
        sum2+=arr[j]
    l1=list()
    l1.append(sum1)
    l1.append(sum2) 
    return l1
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    l=miniMaxSum(arr)
    for i in l:
        print(i,end=" ")
