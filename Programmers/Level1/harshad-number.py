# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x: int) -> bool:
    sum_of_digit, origin = 0, x
    while x > 0:
        sum_of_digit += x % 10
        x //= 10

    if origin % sum_of_digit == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    res = solution(10)
    print(res)

    res = solution(12)
    print(res)

    res = solution(11)
    print(res)

    res = solution(13)
    print(res)
