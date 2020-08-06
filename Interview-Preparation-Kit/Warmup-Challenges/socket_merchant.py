#!/bin/python3

import os
from itertools import groupby


# Complete the sockMerchant function below.
def sockMerchant(ar):
    pairs = 0
    for socks in [len(list(group)) for key, group in groupby(sorted(ar))]:
        pairs += socks//2
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
