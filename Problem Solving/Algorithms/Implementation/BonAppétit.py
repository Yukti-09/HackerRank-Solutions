#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    amt=0
    for i in range(len(bill)):
        if i!=k:
            amt+=bill[i]
    amt=amt/2
    if amt==b:
        print("Bon Appetit")       
    else:
        print(int(b-amt))     
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
