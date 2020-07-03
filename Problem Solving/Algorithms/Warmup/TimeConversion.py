#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    res=""
    st=s.split(":")   
    if st[0]!="12":
        if st[2][2]=="P":
            res+=str(int(st[0])+12)+":"
        elif st[2][2]=="A":
            res+=st[0]+":"
    else:
        if st[2][2]=="P":
            res+="12"+":"
        else:
            res+="00"+":"    
    res+=st[1]+":"+st[2][0]+st[2][1]    
    print(res)
    return res    



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
