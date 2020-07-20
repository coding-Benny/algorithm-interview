#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            negative = negative + 1
        elif arr[i] == 0:
            zero = zero + 1
        elif arr[i] > 0:
            positive = positive + 1
    positive_rate = positive / len(arr)
    negative_rate = negative / len(arr)
    zero_rate = zero / len(arr)
    print("{:.6f}".format(positive_rate))
    print("{:.6f}".format(negative_rate))
    print("{:.6f}".format(zero_rate))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

