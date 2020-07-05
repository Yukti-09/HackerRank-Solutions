#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    st="SOS"
    st1=""
    for i in range(len(s)//3):
        st1+=st
    diff=0
    for i in range(len(s)):
        if st1[i]!=s[i]:
            diff+=1
    print(diff) 
    return diff       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
