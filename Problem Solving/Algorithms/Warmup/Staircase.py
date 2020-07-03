#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    m=1
    while m<=n:
        for i in range(n-m):
            print(" ",end="")
        for j in range(m):
            print("#",end="")
        print()
        m+=1                
if __name__ == '__main__':
    n = int(input())
    staircase(n)
