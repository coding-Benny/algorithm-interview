# https://programmers.co.kr/learn/courses/30/lessons/42862


# my solution
def solution(n, lost, reserve):
    ready = 0
    lost, reserve = sorted([student for student in lost if student not in reserve]), sorted([student for student in reserve if student not in lost])

    for student in lost:
        if student - 1 in reserve:
            ready += 1
            reserve.remove(student - 1)
        elif student + 1 in reserve:
            ready += 1
            reserve.remove(student + 1)
    return n - (len(lost) - ready)


# another solution
def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


def main():
    print(solution(5, [2, 4], [1, 3, 5]))  # 5
    print(solution(5, [2, 4], [3]))  # 4
    print(solution(3, [3], [1]))  # 2
    print(solution(5, [1, 3, 5], [1, 3, 4]))  # 5
    print(solution(5, [2, 3, 4], [3, 4, 5]))  # 4


if __name__ == '__main__':
    main()
