# https://programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter


# my solution
def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).elements())[0]


# another solution
def solution2(participant, completion):
    answer, temp, dic = '', 0, {}

    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))

    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer


# another solution
def solution3(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]


def main():
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # leo
    print(solution2(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))  # vinko
    print(solution3(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))  # mislav


if __name__ == '__main__':
    main()
