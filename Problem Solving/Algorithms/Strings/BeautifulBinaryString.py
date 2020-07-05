#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    b=str(b)
    l=0
    count=0
    while l<=(len(b)-3):
        st=b[l]+b[l+1]+b[l+2]
        if st=="010":
            count+=1
            l+=3
        else:
            l+=1    
    print(count)
    return count    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
