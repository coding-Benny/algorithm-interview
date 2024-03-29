# https://leetcode.com/problems/number-of-islands/
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    def dfs(i, j):
        # # 땅이 아닌 경우
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        # 중복 계산하지 않도록 방문했으면 0으로 표시
        grid[i][j] = 0

        # 동서남북 탐색
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(j, i + 1)
        dfs(j, i - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                # 섬 하나를 전부 탐색했으면 카운트 1 증가
                count += 1
    return count


if __name__ == '__main__':
    print(numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
                      ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
    print(numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                      ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
