#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    cloud = 0

    while cloud < len(c)-1:
        if cloud + 2 <= len(c)-1 and c[cloud + 2] == 0:
            cloud += 2
            jump += 1
        elif c[cloud + 1] == 0:
            cloud += 1
            jump += 1
    return jump

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    #fptr.close()
