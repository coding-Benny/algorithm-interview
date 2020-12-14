#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    prev_height = 0
    cnt = 0
    for i, element in enumerate(s):
        if element == 'U':
            height += 1
        elif element == 'D':
            height -= 1
        if height == 0 and prev_height < 0:
            cnt += 1
        prev_height = height
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
