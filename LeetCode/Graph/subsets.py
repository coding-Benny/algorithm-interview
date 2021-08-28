# https://leetcode.com/problems/subsets/
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


def main():
    print(subsets([1, 2, 3]))  # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    print(subsets([0]))  # [[], [0]]


if __name__ == '__main__':
    main()
