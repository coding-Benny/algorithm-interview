#!/bin/python3

import os


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    min_cost = 0
    c.sort(reverse=True)
    for i in range(len(c)):
        min_cost += (i//k + 1) * c[i]
    return min_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
