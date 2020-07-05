#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    l=list(set(s1))
    l1=list(set(s2))
    count=0
    for i in l:
        if i in l1:
            count+=1
    if(count>0):
        return "YES" 
    else:
        return "NO"          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
