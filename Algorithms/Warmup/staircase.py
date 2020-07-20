#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n-1, -1, -1):
            if j == i:
                break
            print(" ", end="")
            
        for k in range(n):
            print("#", end="")
            if k == i:
                break
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)

