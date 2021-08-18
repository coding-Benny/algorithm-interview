# https://programmers.co.kr/learn/courses/30/lessons/12953
import math


# my solution
def solution(arr):
    divider = 1
    for _ in range(2, max(arr)):
        i = 2
        while i <= max(arr):
            # i로 나눠떨어지는 수가 2개 이상 존재하는 경우
            if len([num for num in arr if num % i == 0]) >= 2:
                quotient = [num // i if num % i == 0 else num for num in arr]
                arr = quotient
                divider *= i
                break
            i += 1

    return divider * math.prod(arr)


# another solution
def solution2(arr):
    answer = arr[0]
    for num in arr:
        answer = num * answer // math.gcd(num, answer)

    return answer


def main():
    print(solution([2, 6, 8, 14]))  # 168
    print(solution([1, 2, 3]))  # 6
    print(solution([2, 8, 10, 16]))  # 80
    print(solution2([2, 50, 80, 100]))  # 400
    print(solution2([3, 4, 9, 16]))  # 144


if __name__ == '__main__':
    main()
