#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rev=s[::-1]
    a=[]
    ar=[]
    for i in range(len(s)-1):
        a.append(abs(ord(s[i])-ord(s[i+1])))
        ar.append(abs(ord(rev[i])-ord(rev[i+1])))
    if a==ar:
        print("Funny")
        return "Funny"
    else:
        print("Not Funny")
        return "Not Funny"    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
