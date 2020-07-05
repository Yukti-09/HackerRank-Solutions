#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    n=bin(n)
    n=str(n)
    n=n[2:]
    l=str()
    if(len(n)<=32):
        for i in range(32-len(n)):
            l+='1'
 
    for i in range(len(n)):
        if(n[i]=='1'):
            l+='0'
        else:
            l+='1'
    return(int(l,2))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
