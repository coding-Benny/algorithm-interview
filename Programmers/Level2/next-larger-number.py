# https://programmers.co.kr/learn/courses/30/lessons/12911
import itertools


def solution(n):
    num, n_bin = 0, "{0:b}".format(n)
    # n보다 1 큰 수부터 2진수로 변환했을 때 1의 갯수가 같은 수를 발견할 때까지 반복
    for num in itertools.count(start=n + 1):
        num_bin = "{0:b}".format(num)
        # 조건을 만족하면 for 문을 탈출
        if n_bin.count('1') == num_bin.count('1'):
            break
    return num


def main():
    print(solution(78))
    print(solution(15))


if __name__ == '__main__':
    main()
