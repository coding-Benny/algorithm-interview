# https://programmers.co.kr/learn/courses/30/lessons/84512
from itertools import product


def solution(word):
    n = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    answer = len(word)
    re = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1
    for i in word:
        answer += re * n[i]
        re = (re - 1) // 5

    return answer


solution2 = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i + 1)]).index(word) + 1


def solution3(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer


def main():
    print(solution("AAAAE"))  # 6
    print(solution2("AAAE"))  # 10
    print(solution2("I"))  # 1563
    print(solution3("EIO"))  # 1189


if __name__ == '__main__':
    main()
