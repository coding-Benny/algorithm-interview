# https://programmers.co.kr/learn/courses/30/lessons/86048


# my solution
def solution(enter, leave):
    must_meet = [0] * len(enter)
    meeting_room = []

    if enter[-1] == leave[0]:  # 제일 마지막 입실한 사람이 제일 먼저 퇴실하는 경우
        return [len(enter) - 1] * len(enter)

    idx = 0
    for i, person in enumerate(enter):
        while meeting_room and leave[idx] in meeting_room:
            meeting_room.remove(leave[idx])
            idx += 1
        meeting_room.append(person)
        if person == leave[idx]:
            for p in meeting_room:
                if must_meet[p - 1] > 0:
                    must_meet[p - 1] += len(meeting_room) - len(set(prev).intersection(meeting_room))
                else:
                    must_meet[p - 1] += len(meeting_room) - 1
            prev = meeting_room[:]
            meeting_room.remove(person)
            idx += 1

    return must_meet


# another solution
def solution2(enter, leave):
    answer = [0] * len(enter)

    room = []
    e_idx = 0
    for l in leave:
        while l not in room:
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l)
        for p in room:
            answer[p - 1] += 1
        answer[l - 1] += len(room)

    return answer


def main():
    print(solution([1, 3, 2], [1, 2, 3]))  # [0, 1, 1]
    print(solution2([1, 4, 2, 3], [2, 1, 3, 4]))  # [2, 2, 1, 3]
    print(solution([3, 2, 1], [2, 1, 3]))  # [1, 1, 2]
    print(solution2([3, 2, 1], [1, 3, 2]))  # [2, 2, 2]
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]))  # [2, 2, 0, 2]
    print(solution2([1, 2, 3], [3, 2, 1]))  # [2, 2, 2]
    print(solution([1, 2, 3], [1, 2, 3]))  # [0, 0, 0]
    print(solution2([1, 2, 3, 4], [3, 4, 2, 1]))  # [3, 3, 2, 2]
    print(solution([1, 2, 3, 4], [4, 2, 1, 3]))  # [3, 3, 3, 3]
    print(solution2([1, 2, 3, 4, 5], [5, 3, 1, 2, 4]))  # [4, 4, 4, 4, 4]
    print(solution([1, 4, 5, 3, 2], [5, 4, 3, 2, 1]))  # [4, 1, 1, 2, 2]
    print(solution2([1, 3, 2, 4, 6, 5, 8, 7, 9, 10], [9, 5, 1, 10, 7, 4, 8, 6, 2, 3]))  # [8, 9, 9, 9, 8, 9, 9, 9, 8, 6]
    print(solution([1, 10, 9, 2, 3, 8, 7, 4, 5, 6], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # [9, 7, 7, 5, 5, 5, 3, 3, 1, 1]


if __name__ == '__main__':
    main()