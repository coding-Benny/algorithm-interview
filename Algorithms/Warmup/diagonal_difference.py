#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                left_to_right = left_to_right + arr[i][j]
            if i+j == len(arr)-1:
                right_to_left = right_to_left + arr[i][j]
    result = abs(left_to_right - right_to_left)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

