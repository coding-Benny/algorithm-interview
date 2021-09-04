# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


# my solution
def solution(priorities, location):
    printer, waiting = [], priorities[:]
    priorities = deque(priorities)

    for i, priority in enumerate(priorities):
        priorities[i] = (i, priority)

    while True:
        # 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        j = priorities[0]
        # 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면
        #    J를 대기목록의 가장 마지막에 넣습니다.
        if any([prior[1] for prior in priorities if prior[1] > j[1]]):
            priorities.popleft()
            priorities.append(j)
        else:     # 3. 그렇지 않으면 J를 인쇄합니다.
            printer.append(j[0])
            priorities.popleft()

        if len(printer) == len(waiting):
            break

    return printer.index(location) + 1


# another solution
def solution2(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


# another solution
def solution3(priorities, location):
    ans = 0
    m = max(priorities)
    while True:
        v = priorities.pop(0)
        if m == v:
            ans += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(v)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return ans


# another solution
def solution4(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer


# another solution
def solution5(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor % jobs]:
            priorities[cursor % jobs] = 0
            answer += 1
            if cursor % jobs == location:
                break
        cursor += 1
    return answer


def main():
    print(solution([2, 1, 3, 2], 2))  # 1
    print(solution2([1, 1, 9, 1, 1, 1], 0))  # 5
    print(solution3([2, 1, 3, 2], 2))  # 1
    print(solution4([1, 1, 9, 1, 1, 1], 0))  # 5
    print(solution5([2, 1, 3, 2], 2))  # 1


if __name__ == '__main__':
    main()
