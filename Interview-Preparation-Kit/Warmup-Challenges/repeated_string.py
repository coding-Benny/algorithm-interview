#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    # first trial
    # text = ""
    # count = 0
    # for i in range(n):
    #     text += s
    # substr = text[:n]
    # for character in range(len(substr)):
    #     if substr[character] == 'a':
    #         count += 1
    # return count

    # second trial
    # text = ""
    # count = 0
    # text = s * n
    # substr = text[:n]
    # return substr.count('a')

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    #fptr.close()
