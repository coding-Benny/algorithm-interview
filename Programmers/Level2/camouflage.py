# https://programmers.co.kr/learn/courses/30/lessons/42578
import collections
from functools import reduce


def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer


def solution2(c):
    return reduce(lambda x, y: x * y, [a + 1 for a in collections.Counter([x[1] for x in c]).values()]) - 1


def solution3(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


def main():
    print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5
    print(solution2([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))  # 3
    print(solution3([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))  # 5


if __name__ == '__main__':
    main()
