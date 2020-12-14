#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    temp = 0
    count = 0
    for i in range(len(a)):
        for j in range(0, len(a)-1):
            if a[j] > a[j+1]:
                count += 1
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
