#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_list = []
    pair = []
    arr = list(set(ar))
    for i in range(len(arr)):
        count = 0
        for j in range(n):
            if arr[i] == ar[j]:
                count += 1
        count_list.append(count)
    for k in range(len(count_list)):
        pair.append(count_list[k]//2)
    return sum(pair)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')
    #fptr.close()
