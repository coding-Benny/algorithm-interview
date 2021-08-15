# https://programmers.co.kr/learn/courses/30/lessons/12941

# my solution
def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    sum = 0

    for i in range(len(A)):
        sum += A[i] * B[i]

    return sum


# another solution
def solution2(A, B):
    return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))


def main():
    print(solution([1, 4, 2], [5, 4, 4]))  # 29
    print(solution2([1, 2], [3, 4]))  # 10


if __name__ == '__main__':
    main()
