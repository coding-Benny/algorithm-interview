# https://programmers.co.kr/learn/courses/30/lessons/86048


# my solution 11/37
def solution(enter, leave):
    must_meet = [0] * len(enter)
    meeting_room = []

    if enter[-1] == leave[0]:  # 제일 마지막 입실한 사람이 제일 먼저 퇴실하는 경우
        return [len(enter) - 1] * len(enter)

    # if enter[0] == leave[0] or enter[-1] == leave[-1]:  # 제일 먼저/마지막 입실한 사람이 제일 먼저/마지막 퇴실하는 경우
    #     pass
    #
    # if enter[0] == leave[-1]:  # 제일 먼저 입실한 사람이 제일 마지막에 퇴실하는 경우
    #     must_meet[enter[0] - 1] += len(enter) - 1

    idx = 0
    for i, person in enumerate(enter):
        if leave[idx] in meeting_room:
            meeting_room.remove(leave[idx])
            idx += 1
        meeting_room.append(person)
        if person == leave[idx]:
            for p in meeting_room:
                must_meet[p - 1] += len(meeting_room) - 1
            meeting_room.remove(person)
            idx += 1

    return must_meet


def main():
    print(solution([1, 3, 2], [1, 2, 3]))  # [0, 1, 1]
    print(solution([1, 4, 2, 3], [2, 1, 3, 4]))  # [2, 2, 1, 3]
    print(solution([3, 2, 1], [2, 1, 3]))  # [1, 1, 2]
    print(solution([3, 2, 1], [1, 3, 2]))  # [2, 2, 2]
    print(solution([1, 4, 2, 3], [2, 1, 4, 3]))  # [2, 2, 0, 2]


if __name__ == '__main__':
    main()
