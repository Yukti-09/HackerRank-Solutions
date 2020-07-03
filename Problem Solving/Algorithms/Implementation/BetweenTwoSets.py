#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    
    counter=0
    for i in range(1,max(b)+1):
        count=0
        for j in a:
            if i%j==0:
                count+=1
        for k in b:
            if k%i==0:
                count+=1
        if count==(len(a)+len(b)):
            counter+=1
    print(counter)
    return counter                       

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
