#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    max1=0
    for i in word:
        w=ord(i)-97
        for i in range(len(h)):
            if w==i:
                if max1<h[i]:
                    max1=h[i]
    print(max1*len(word))
    return (max1*len(word))              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
