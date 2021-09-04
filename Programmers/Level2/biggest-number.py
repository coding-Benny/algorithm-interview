# https://programmers.co.kr/learn/courses/30/lessons/42746


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


def main():
    print(solution([6, 10, 2]))  # "6210"
    print(solution([3, 30, 34, 5, 9]))  # "9534330"
    print(solution([0, 0]))  # "0"
    print(solution([33, 30, 3]))  # "33330"
    print(solution([6, 646]))  # "6646"
    print(solution([383, 38]))  # "38383"
    print(solution([838, 83]))  # "83883"


if __name__ == '__main__':
    main()
