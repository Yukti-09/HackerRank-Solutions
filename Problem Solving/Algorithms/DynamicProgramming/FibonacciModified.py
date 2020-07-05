#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
    l=[]
    l.append(t1)
    l.append(t2)
    for i in range(n-2):
        c=(t1)+(t2*t2)
        l.append((t1)+(t2*t2))
        t1=t2
        t2=c
       
    print(l[n-1])    
    return l[n-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
