# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total


def solution1(a, b):
    product = [a[i] * b[i] for i in range(len(a))]
    return sum(product)


if __name__ == '__main__':
    res = solution([1, 2, 3, 4], [-3, -1, 0, 2])
    print(res)
    res = solution1([-1, 0, 1], [1, 0, -1])
    print(res)
