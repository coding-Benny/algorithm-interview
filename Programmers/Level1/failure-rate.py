# https://programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter


def solution(N: int, stages: list) -> list:
    failure_rate = []
    current_stage = Counter(stages)
    num_of_users = len(stages)
    for i in range(1, N + 1):
        if num_of_users <= 0:
            failure_rate.append((i, 0))
        else:
            failure_rate.append((i, current_stage[i] / num_of_users))
        num_of_users -= current_stage[i]

    failure_rate = sorted(failure_rate, key=lambda x: x[1], reverse=True)
    return [stage[0] for stage in failure_rate]


if __name__ == '__main__':
    res = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
    print(res)
    res = solution(4, [4, 4, 4, 4, 4])
    print(res)
    res = solution(5, [2, 1, 2, 4, 2, 4, 3, 3])
    print(res)
