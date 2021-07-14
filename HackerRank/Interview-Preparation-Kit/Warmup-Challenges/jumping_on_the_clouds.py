#!/bin/python3


# Complete the jumpingOnClouds function below.
def jumpingOnClouds1(c):
    jump = 0
    cloud = 0

    while cloud < len(c)-1:
        if cloud + 2 <= len(c)-1 and c[cloud + 2] == 0:
            cloud += 2
            jump += 1
        elif c[cloud + 1] == 0:
            cloud += 1
            jump += 1
    return jump


def jumpingOnClouds2(c):
    step, jump = 0, 0
    while step + 1 < len(c):
        if step + 2 < len(c) and c[step + 2] == 0:
            step += 2
        else:
            step += 1
        jump += 1
    return jump


if __name__ == '__main__':
    result = jumpingOnClouds1([0, 0, 1, 0, 0, 1, 0])
    print(result)

    result = jumpingOnClouds2([0, 0, 0, 1, 0, 0])
    print(result)
