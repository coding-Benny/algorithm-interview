#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletion = 0
    str = list(s)
    for idx in range(len(str)-1):
        if str[idx] == str[idx+1]:
            deletion += 1
    return deletion

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)
        print(str(result) + '\n')
        fptr.write(str(result) + '\n')

    fptr.close()
