#!/bin/python3


# Complete the hourglassSum function below.
def hourglassSum1(arr):
    values = []
    for i in range(4):
        for j in range(4):
            sum = 0
            for k in range(3):
                sum += arr[i][j+k]
                sum += arr[i+2][j+k]
            sum += arr[i+1][j+1]
            values.append(sum)
    return max(values)


def hourglassSum2(arr):
    sum_list = []
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[0]) - 1):
            total = 0
            total += arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1]
            total += arr[i][j]
            total += arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            sum_list.append(total)
    return max(sum_list)


if __name__ == '__main__':
    result = hourglassSum1([
        [-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]
    ])
    print(result)

    result = hourglassSum2([
        [1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]
    ])
    print(result)
