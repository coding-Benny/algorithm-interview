# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total


if __name__ == '__main__':
    res = solution(12)
    print(res)

    res = solution(5)
    print(res)