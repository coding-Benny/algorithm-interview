# https://programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter


def solution(nums: list) -> int:
    phoneketmon_type = Counter(nums)
    if len(phoneketmon_type) < len(nums) // 2:
        return len(phoneketmon_type)
    else:
        return len(nums) // 2


if __name__ == '__main__':
    res = solution([3, 1, 2, 3])
    print(res)
    res = solution([3, 3, 3, 2, 2, 4])
    print(res)
    res = solution([3, 3, 3, 2, 2, 2])
    print(res)
