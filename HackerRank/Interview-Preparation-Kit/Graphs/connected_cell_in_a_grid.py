#!/bin/python3

import os


# Complete the maxRegion function below.
def get_region_size(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return 0
    if grid[row][col] == 0:
        return 0
    grid[row][col] = 0
    size = 1
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r != row or c != col:
                size += get_region_size(grid, r, c)
    return size


def maxRegion(grid):
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                size = get_region_size(grid, row, col)
                count = max(size, count)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
