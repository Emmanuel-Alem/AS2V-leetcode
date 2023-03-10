#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#



def gradingStudents(grades):
    # Write your code here
    l = []
    for grade in grades:
         
        if grade < 38:
            l.append(grade)
        elif grade % 5 == 0:
            l.append(grade)
        else:
            next_multiple_five = (grade + 5) - (grade % 5)
            if next_multiple_five - grade < 3:
                l.append(next_multiple_five)
            else:
                l.append(grade)
    return l        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
