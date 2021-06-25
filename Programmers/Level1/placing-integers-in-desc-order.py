# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n: int) -> int:
    return int(''.join(sorted(list(str(n)), reverse=True)))


if __name__ == '__main__':
    res = solution(118372)
    print(res)
