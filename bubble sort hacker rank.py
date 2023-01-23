#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(b):
    # Write your code here
    
    s = 0
    for i in range(len(b)):
        
        for j in range(len(b) - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                s += 1
    print(f'Array is sorted in {s} swaps.')
    print(f'First Element: {b[0]}')
    print(f'Last Element: {b[-1]}')
    

      
        
    


if __name__ == '__main__':
    n = int(input().strip())

    b = list(map(int, input().rstrip().split()))
    
    countSwaps(b)

    
