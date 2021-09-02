# https://programmers.co.kr/learn/courses/30/lessons/70129


# my solution
def solution(s):
    step = count = 0
    # s가 "1"이 될 때까지 계속해서 s에 이진 변환
    while s != "1":
        step += 1
        count += s.count('0')
        # 1. s의 모든 0을 제거
        s = s.replace('0', '')
        # 2. s의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꾼다.
        s = "{0:b}".format(len(s))
    return [step, count]


# another solution
def solution2(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]


def main():
    print(solution("110010101001"))  # [3, 8]
    print(solution("01110"))  # [3, 3]
    print(solution2("1111111"))  # [4, 1]


if __name__ == '__main__':
    main()
