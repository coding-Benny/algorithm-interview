# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n: int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total


if __name__ == '__main__':
    res = solution(123)
    print(res)

    res = solution(987)
    print(res)
