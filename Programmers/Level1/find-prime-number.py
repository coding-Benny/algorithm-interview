# https://programmers.co.kr/learn/courses/30/lessons/12921
def solution(n: int) -> int:
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, int((n + 1) ** 0.5) + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return len([i for i in range(2, n + 1) if sieve[i]])


# another solution
def solution2(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


if __name__ == '__main__':
    print(solution(10))  # 4
    print(solution2(5))  # 3
