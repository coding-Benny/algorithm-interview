# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


def solution2(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        q, r = divmod(n - 1, 3)
        return solution2(q) + '124'[r]


def main():
    print(solution(1))  # 1
    print(solution(2))  # 2
    print(solution2(3))  # 4
    print(solution2(4))  # 11


if __name__ == '__main__':
    main()
