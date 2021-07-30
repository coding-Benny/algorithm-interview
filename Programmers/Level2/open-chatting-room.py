from collections import defaultdict


def solution(record):
    users = defaultdict(dict)
    result = []

    for rec in record:
        user_info = rec.split()
        action, user_id = user_info[0], user_info[1]
        if action == 'Enter' or action == 'Change':
            nickname = user_info[2]
            users[user_id] = nickname

    for rec in record:
        user_info = rec.split()
        action, user_id = user_info[0], user_info[1]
        if action == 'Enter':
            result.append("{}님이 들어왔습니다.".format(users.get(user_id)))
        elif action == 'Leave':
            result.append("{}님이 나갔습니다.".format(users.get(user_id)))

    return result


def main():
    print(solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))


if __name__ == '__main__':
    main()
