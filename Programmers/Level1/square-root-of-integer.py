# https://programmers.co.kr/learn/courses/30/lessons/12934
import math


def solution(n: int):
    if math.sqrt(n).is_integer():
        return (math.sqrt(n) + 1) ** 2
    return -1


if __name__ == '__main__':
    res = solution(121)
    print(res)

    res = solution(3)
    print(res)
