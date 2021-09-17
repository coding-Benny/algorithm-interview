# https://programmers.co.kr/learn/courses/30/lessons/42746
import functools


def to_swap(n1, n2):
    return str(n1) + str(n2) < str(n2) + str(n1)


# my solution - Time out(54.5/100.0)
def solution(numbers):
    i = 1
    while i < len(numbers):
        j = i
        while j > 0 and to_swap(numbers[j - 1], numbers[j]):
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            j -= 1
        i += 1
    return str(''.join(map(str, numbers))) if numbers[0] != 0 else "0"


# another solution
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크다면 1, t2가 크다면 -1,같으면 0


# another solution
def solution3(numbers):
    n = [str(x) for x in numbers]
    n.sort(key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))


def main():
    print(solution([6, 10, 2]))  # "6210"
    print(solution([3, 30, 34, 5, 9]))  # "9534330"
    print(solution([0, 0]))  # "0"
    print(solution2([33, 30, 3]))  # "33330"
    print(solution2([6, 646]))  # "6646"
    print(solution2([383, 38]))  # "38383"
    print(solution3([838, 83]))  # "83883"
    print(solution3([23, 232, 21, 212]))  # "2323221221"
    print(solution3([9, 997, 99, 878, 87]))  # "99999787887"


if __name__ == '__main__':
    main()
