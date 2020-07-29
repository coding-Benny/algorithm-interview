#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    binary = '{0:0b}'.format(n).zfill(32)
    flipping_binary = ""
    for i in binary:
        if i == "0":
            flipping_binary += "1"
        else:
            flipping_binary += "0"
    return int(flipping_binary, 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
