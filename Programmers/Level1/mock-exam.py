# https://programmers.co.kr/learn/courses/30/lessons/42840
from itertools import cycle


# my solution
def solution(answers):
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    corrections = []
    for i, student in enumerate(students):
        count = len(answers) // len(student)
        if len(answers) % len(student) != 0:
            count += 1
        students[i] = student * count

    for i, student in enumerate(students):
        students[i] = [response - answer for (response, answer) in zip(student, answers)]

    for student in students:
        corrections.append(student.count(0))

    top = max(corrections)
    return [i + 1 for i in range(len(corrections)) if corrections[i] == top]


# another solution
def solution2(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx % len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx % len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result


# another solution
def solution3(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


# another solution
def solution4(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]


def main():
    print(solution([1, 2, 3, 4, 5]))  # [1]
    print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]
    print(solution2([3, 3, 1, 1, 1, 1, 2, 3, 4, 5]))  # [1, 3]
    print(solution2([4, 5, 5, 2, 1]))  # [1, 2, 3]
    print(solution3([2, 1, 2, 3, 2, 4, 2, 5]))  # [2]
    print(solution3([5, 5, 5, 1, 4, 1]))  # [1, 3]
    print(solution4([1, 2, 3]))  # [1]
    print(solution4([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))  # [1]


if __name__ == '__main__':
    main()
