#!/bin/python3


# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:] + a[:d]

if __name__ == '__main__':
    result = rotLeft([1, 2, 3, 4, 5], 4)
    print(result)
