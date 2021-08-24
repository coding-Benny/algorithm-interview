# https://programmers.co.kr/learn/courses/30/lessons/64065
import re
from collections import Counter


# my solution
def solution(s):
    s = s[1:-1].split("},")
    s = [tup.replace('{', '').replace('}', '') for tup in s]
    my_tuple = []

    for elems in sorted(s, key=len):
        elem = elems.split(',')
        for e in elem:
            if e not in my_tuple:
                my_tuple.append(e)

    return list(map(int, my_tuple))


# another solution
def solution2(s):
    s = Counter(re.findall(r'\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


# another solution
def solution3(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key=len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


def main():
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
    print(solution2("{{20,111},{111}}"))  # [111, 20]
    print(solution2("{{123}}"))  # [123]
    print(solution3("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]


if __name__ == '__main__':
    main()
