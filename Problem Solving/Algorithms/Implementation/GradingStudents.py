#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    grades_copy=[]
    for i in grades:
        flag=0
        if(i<38):
            grades_copy.append(i)
        else:
            for j in range(0,3):
                if((i+j)%5==0):
                    flag=1
                    grades_copy.append(i+j)
            if(flag==0):
                grades_copy.append(i)
    return grades_copy                    

    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    for i in result:
        print(i)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
