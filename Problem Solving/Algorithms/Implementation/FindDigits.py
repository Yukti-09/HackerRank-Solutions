#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    m=n 
    digits=[]
    while m:
        digits.append(m%10)
        m=m//10
    res=0    
    for i in range(len(digits)):
        if digits[i]!=0:
            if n%digits[i]==0 :
                res+=1
    return res        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
