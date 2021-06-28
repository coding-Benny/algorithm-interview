# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers: list, hand: str) -> str:
    result = ''
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    lcur, rcur = (3, 0), (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            result += 'L'
            for i, row in enumerate(phone):
                if row[0] == number:
                    lcur = (i, 0)
                    break
        elif number in [3, 6, 9]:
            result += 'R'
            for i, row in enumerate(phone):
                if row[2] == number:
                    rcur = (i, 2)
                    break
        else:
            cur = tuple()
            for i, row in enumerate(phone):
                for j in range(len(phone[i])):
                    if phone[i][j] == number:
                        cur = (i, j)
                        break

            lgap = abs(lcur[0] - cur[0]) + abs(lcur[1] - cur[1])
            rgap = abs(rcur[0] - cur[0]) + abs(rcur[1] - cur[1])

            if lgap < rgap:
                result += 'L'
                lcur = cur
            elif lgap > rgap:
                result += 'R'
                rcur = cur
            else:
                if hand == "left":
                    result += 'L'
                    lcur = cur
                else:
                    result += 'R'
                    rcur = cur
    return result


if __name__ == '__main__':
    res = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
    print(res)
    res = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
    print(res)
    res = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
    print(res)
