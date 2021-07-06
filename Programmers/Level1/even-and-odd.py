# https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == '__main__':
    res = solution(3)
    print(res)

    res = solution(4)
    print(res)
