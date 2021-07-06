# https://programmers.co.kr/learn/courses/30/lessons/12940

def isPrime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(n: int, m: int) -> list:
    if isPrime(n) and isPrime(m):
        return [1, n * m]
    else:
        factor, i = 1, 2
        iteration = n if n < m else m
        while n > 1 and m > 1 and i <= iteration:
            if n % i == 0 and m % i == 0:
                n //= i
                m //= i
                factor *= i
                i = 2
                continue
            i += 1
        if factor == 1:
            return [1, n * m]
        return [factor, factor * n * m]


if __name__ == '__main__':
    res = solution(3, 12)
    print(res)

    res = solution(2, 5)
    print(res)

    res = solution(35, 17)
    print(res)

    res = solution(4, 20)
    print(res)
