# https://programmers.co.kr/learn/courses/30/lessons/68935


def convert_ternary(num):
    remains = []
    while num > 0:
        r = num % 3
        num //= 3
        remains.append(r)
    return remains


def convert_decimal(t):
    decimal = 0
    for i, n in enumerate(t):
        decimal += (3 ** i) * n
    return decimal


# my solution
def solution(n):
    ternary = convert_ternary(n)[::-1]
    return convert_decimal(ternary)


# another solution
def solution2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


def main():
    print(solution(45))
    print(solution2(125))


if __name__ == '__main__':
    main()
