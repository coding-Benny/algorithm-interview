# https://programmers.co.kr/learn/courses/30/lessons/62048
import math


# my solution(88.9/100.0 - Time over)
def solution(w, h):
    if w == h:
        return w * (h - 1)

    if w == 1 or h == 1:
        return 0

    tan = h / w
    count = 0

    for height in range(1, h):
        width = height / tan
        count += int(math.floor(width))

    return count * 2


# another solution
def solution2(w, h):
    return w * h - (w + h - math.gcd(w, h))


def main():
    print(solution(8, 12))
    print(solution(4, 4))
    print(solution2(10000000, 99999999))  # 999999880000002


if __name__ == '__main__':
    main()
