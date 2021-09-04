# https://programmers.co.kr/learn/courses/30/lessons/42586
from math import ceil


# my solution
def solution(progresses, speeds):
    deploy = []
    while True:
        for i, (progress, speed) in enumerate(zip(progresses, speeds)):
            progresses[i] += speed

        if progresses[0] >= 100:
            tmp = []
            for i, prog in enumerate(progresses):
                if prog < 100:
                    break
                tmp.append(prog)
            deploy.append(len(tmp))
            progresses, speeds = progresses[i:], speeds[i:]

        if len(progresses) == 1 and progresses[0] >= 100:
            break
    return deploy


# another solution
def solution2(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


# another solution
def solution3(progresses, speeds):
    answer = []
    time, count = 0, 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


# another solution
def solution4(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList


def main():
    print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
    print(solution2([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
    print(solution3([93, 30, 55], [1, 30, 5]))  # [2, 1]
    print(solution4([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]


if __name__ == '__main__':
    main()
