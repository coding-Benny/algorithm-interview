# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# my solution
def solution(nums):
    count = 0
    for comb in list(combinations(nums, 3)):
        if is_prime(sum(comb)):
            count += 1
    return count


def prime_number(x):
    answer = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0


# another solution
def solution2(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums, 3)])


def main():
    print(solution([1, 2, 3, 4]))  # 1
    print(solution([1, 2, 7, 6, 4]))  # 4


if __name__ == '__main__':
    main()
