#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count=0
    count_num=0
    count_lower=0
    count_upper=0
    count_special=0
    numbers = "0123456789"
    numbers=list(numbers)
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    lower_case=list(lower_case)
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper_case=list(upper_case)
    special_characters = "!@#$%^&*()-+"
    special_characters=list(special_characters)
    for i in password:
        if i in numbers:
            count_num+=1
        elif i in upper_case:
            count_upper+=1
        elif i in lower_case:
            count_lower+=1
        elif i in special_characters:
            count_special+=1
    if count_num==0:
        count+=1
    if count_lower==0:
        count+=1
    if count_special==0:
        count+=1
    if count_upper==0:
        count+=1
    
    if 6-n>count:
        count=6-n
    print(count)
    return count    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
