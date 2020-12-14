#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    values = []
    for i in range(4):
        for j in range(4):
            sum = 0
            for k in range(3):
                sum += arr[i][j+k]
                sum += arr[i+2][j+k]
            sum += arr[i+1][j+1]
            values.append(sum)
    return max(values)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
