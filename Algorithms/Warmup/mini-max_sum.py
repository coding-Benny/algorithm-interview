#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    arr.sort()
    for i in range(len(arr)-1):
        minimum = minimum + arr[i]
    for j in range(len(arr)-1, 0, -1):
        maximum = maximum + arr[j]
    print(minimum, maximum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

