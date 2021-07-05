# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left: int, right: int) -> int:
    result = 0
    for number in range(left, right + 1):
        count = 0
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1

        if count % 2 == 0:
            result += number
        else:
            result -= number
    return result


if __name__ == '__main__':
    res = solution(13, 17)
    print(res)

    res = solution(24, 27)
    print(res)
