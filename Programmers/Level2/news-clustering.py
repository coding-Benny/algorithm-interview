# https://programmers.co.kr/learn/courses/30/lessons/17677
import re
from math import floor
from collections import Counter


def solution(str1, str2):
    set1, set2, str1, str2 = [], [], str1.upper(), str2.upper()

    for i in range(len(str1) - 1):
        if re.search('[a-zA-Z]', str1[i]) and re.search('[a-zA-Z]', str1[i + 1]):
            set1.append(str1[i] + str1[i + 1])

    for i in range(len(str2) - 1):
        if re.search('[a-zA-Z]', str2[i]) and re.search('[a-zA-Z]', str2[i + 1]):
            set2.append(str2[i] + str2[i + 1])

    if not set1 and not set2:
        return 65536
    elif not set1 and set2:
        return 0

    intersection = list((Counter(set1) & Counter(set2)).elements())
    a_set = list((Counter(set1) - Counter(intersection)).elements())
    b_set = list((Counter(set2) - Counter(intersection)).elements())
    union = intersection + a_set + b_set

    return floor(len(intersection) / len(union) * 65536)


def main():
    print(solution("FRANCE", "french"))  # 16384
    print(solution("handshake", "shake hands"))  # 65536
    print(solution("aa1+aa2", "AAAA12"))  # 43690
    print(solution("E=M*C^2", "e=m*c^2"))  # 65536
    print(solution("aa1+aa2", "AA12"))  # 32768
    print(solution("aaaa+bbb", "aaa+bbbb"))  # 43690


if __name__ == '__main__':
    main()
