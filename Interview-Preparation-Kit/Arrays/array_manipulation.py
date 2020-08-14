#!/bin/python3

import os


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    tmp = 0
    maximum = -1

    for query in queries:
        start = query[0] - 1
        end = query[1]

        arr[start] += query[2]
        arr[end] -= query[2]

    for val in arr:
        tmp += val
        if maximum < tmp:
            maximum = tmp
    return maximum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
