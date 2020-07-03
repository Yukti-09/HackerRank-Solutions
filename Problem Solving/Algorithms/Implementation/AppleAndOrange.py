#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count1=0
    count2=0
    for i in range(len(apples)):
        apples[i]+=a
    for i in range(len(oranges)):
        oranges[i]+=b
    for i in apples:
        if i>=s and i<=t:
            count1+=1       
    for i in oranges:
        if i>=s and i<=t:
            count2+=1
    print(count1) 
    print(count2)    



if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)
