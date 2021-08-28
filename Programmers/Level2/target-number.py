# https://programmers.co.kr/learn/courses/30/lessons/43165
from itertools import product


def solution(numbers, target):
    answer = 0

    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    dfs(0, 0)
    return answer


def solution2(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


def main():
    print(solution([1, 1, 1, 1, 1], 3))  # 5
    print(solution2([1, 2, 3, 4, 5], 5))  # 3
    print(solution3([1, 2, 3, 4, 5], 7))  # 2


if __name__ == '__main__':
    main()
