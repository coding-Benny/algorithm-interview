# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n: int) -> list:
    answer = []
    while n > 0:
        answer.append(n % 10)
        n //= 10
    return answer


if __name__ == '__main__':
    res = solution(12345)
    print(res)
