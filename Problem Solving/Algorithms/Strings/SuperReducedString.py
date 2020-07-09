#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    x=len(s)
    l=0
    while(l<x-1):
        if(s[l]==s[l+1]):
            s=s[:l]+s[l+1:]
            s=s[:l]+s[l+1:]
            l=0
            x=len(s)
        else:
            l+=1
            
    if(s==''):
        return('Empty String')
    else:
        return(s)
  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
