# https://programmers.co.kr/learn/courses/30/lessons/86051


# my solution
def solution(numbers):
    sum = 0
    for i in range(10):
        if i not in numbers:
            sum += i
    return sum


# my solution
def solution2(numbers):
    return sum([i for i in range(10) if i not in numbers])


# another solution
def solution3(numbers):
    return 45 - sum(numbers)


def main():
    print(solution([1, 2, 3, 4, 6, 7, 8, 0]))  # 14
    print(solution2([5, 8, 4, 0, 6, 7, 9]))  # 6


if __name__ == '__main__':
    main()
