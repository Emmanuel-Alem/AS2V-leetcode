#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    s = 0
    v = 0
    flag = True
    for i in range(steps):
        if path[i] == 'U':
            s += 1
        else:
            s -= 1
        if s < 0:
            flag = False
        if not flag:
            if s == 0:
                flag = True
                v += 1 
    return v
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
