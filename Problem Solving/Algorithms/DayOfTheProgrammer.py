#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap=0
    sum=0
    if(year%400==0 or(year%4==0 and year%100!=0) or (year<=1917 and year%4==0)):
        leap=1
    if year==1918:
        return'26.09.1918'
    if(leap==0):
        st='13.09.'+str(year)
    else:
        st='12.09.'+str(year)
    return st
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
