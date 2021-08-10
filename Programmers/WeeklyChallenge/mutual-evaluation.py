# https://programmers.co.kr/learn/courses/30/lessons/83201
from collections import Counter


# my solution
def solution(scores):
    grade = ''

    for j in range(len(scores[0])):
        total, count, receives = 0, 0, []

        for i in range(len(scores)):
            receives.append(scores[i][j])

        min_idx = receives.index(min(receives))
        max_idx = receives.index(max(receives))

        for k, receive in enumerate(receives):
            if j == k and (j == min_idx or j == max_idx):
                if receives.count(receive) == 1:
                    continue
                else:
                    total += receive
                    count += 1
            else:
                total += receive
                count += 1

        avg = total / count
        if avg >= 90:
            grade += 'A'
        elif 80 <= avg < 90:
            grade += 'B'
        elif 70 <= avg < 80:
            grade += 'C'
        elif 50 <= avg < 70:
            grade += 'D'
        elif avg < 50:
            grade += 'F'
    return grade


# another solution
def solution2(scores):
    answer = ''

    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1

        grade = sum(score) / length

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


def main():
    print(solution([[100, 90, 98, 88, 65],
                    [50, 45, 99, 85, 77],
                    [47, 88, 95, 80, 67],
                    [61, 57, 100, 80, 65],
                    [24, 90, 94, 75, 65]]))
    print(solution([[50, 90], [50, 87]]))
    print(solution2([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))
    print(solution2([[75, 50, 100], [75, 100, 20], [100, 100, 20]]))


if __name__ == '__main__':
    main()
