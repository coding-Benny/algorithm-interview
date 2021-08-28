# https://leetcode.com/problems/combination-sum/
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위원소까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
            # 순열 문제였다면 항상 첫 번째 값부터 탐색하도록 인덱스를 0으로 함
            # dfs(csum - candidates[i], 0, path + [candidates[i]])

    dfs(target, 0, [])
    return result


def main():
    print(combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
    print(combinationSum([2, 3, 5], 8))  # [[2,2,2,2],[2,3,3],[3,5]]
    print(combinationSum([2], 1))  # []
    print(combinationSum([1], 1))  # [[1]]
    print(combinationSum([1], 2))  # [[1, 1]]


if __name__ == '__main__':
    main()
