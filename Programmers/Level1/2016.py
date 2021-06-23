from enum import Enum

Day = Enum('Day', 'SUN MON TUE WED THU FRI SAT')


def solution(a, b) -> str:
    day = Day.FRI.value
    dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if a == 1:
        total = (b - 1) % 7
    else:
        total = sum(dates[:a - 1]) + b - 1
    gap = total % 7
    if day + gap > 7:
        day = Day((day + gap) % 7).name
    else:
        day = Day(day + gap).name
    return day


if __name__ == '__main__':
    res = solution(1, 18)
    print(res)
    res = solution(5, 24)
    print(res)
    res = solution(2, 10)
    print(res)
    res = solution(6, 16)
    print(res)
    res = solution(8, 12)
    print(res)
    res = solution(12, 10)
    print(res)
    res = solution(10, 23)
    print(res)

