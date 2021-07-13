#!/bin/python3

from itertools import groupby
from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant1(n, ar):
    pairs = 0
    for socks in [len(list(group)) for key, group in groupby(sorted(ar))]:
        pairs += socks//2
    return pairs


def sockMerchant2(n, ar):
    pair = 0
    counter = Counter(ar)
    for item in counter.items():
        pair += item[1] // 2
    return pair


if __name__ == '__main__':
    result = sockMerchant1(7, [1, 2, 1, 2, 1, 3, 2])
    print(result)
    
    result = sockMerchant2(9, [10, 20, 20, 10, 10, 30, 50, 20, 10])
    print(result)
