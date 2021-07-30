# https://programmers.co.kr/learn/courses/30/lessons/12945

def solution1(n):
    fibos = [0, 1]

    for i in range(2, n + 1):
        fibos.append((fibos[i - 2] + fibos[i - 1]) % 1234567)

    return fibos[-1]


def solution2(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, (a + b) % 1234567
    return a


def main():
    print(solution1(3))
    print(solution1(5))
    print(solution1(1234567))


if __name__ == '__main__':
    main()
