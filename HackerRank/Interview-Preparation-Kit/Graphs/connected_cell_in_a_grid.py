# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem

# !/bin/python3

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

# my solution
def maxRegion(grid):
    def dfs(i, j):
        count = 0

        # 범위 체크
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0

        # 방문 표시
        grid[i][j] = 0
        count += 1

        # 동서남북, 대각선 탐색
        count += dfs(i - 1, j + 1)
        count += dfs(i, j + 1)
        count += dfs(i + 1, j + 1)
        count += dfs(i - 1, j)
        count += dfs(i + 1, j)
        count += dfs(i - 1, j - 1)
        count += dfs(i, j - 1)
        count += dfs(i + 1, j - 1)

        return count

    region = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                cnt = dfs(i, j)
                if region <= cnt:
                    region = cnt
    return region


# another solution
def get_region_size(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]):
        return 0
    if grid[row][col] == 0:
        return 0
    grid[row][col] = 0
    size = 1
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if r != row or c != col:
                size += get_region_size(grid, r, c)
    return size


def maxRegion2(grid):
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                size = get_region_size(grid, row, col)
                count = max(size, count)
    return count


# another solution
def getBiggestRegion(grid):
    def dfs(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + sum(dfs(i2, j2) for i2 in range(i - 1, i + 2) for j2 in range(j - 1, j + 2))
        return 0

    return max(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))


if __name__ == '__main__':
    print(maxRegion(
        [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ]
    ))  # 5
    print(maxRegion2(
        [
            [0, 0, 1, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
    ))  # 8
    print(getBiggestRegion(
        [
            [1, 0, 1, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0]
        ]
    ))  # 10
