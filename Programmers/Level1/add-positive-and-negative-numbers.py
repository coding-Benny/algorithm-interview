def solution(absolutes: list, signs: list) -> int:
    total = 0
    for i, number in enumerate(absolutes):
        if not signs[i]:
            absolutes[i] *= -1
        total += absolutes[i]
    return total


if __name__ == '__main__':
    res = solution([4, 7, 12], [True, False, True])
    print(res)
    res = solution([1, 2, 3], [False, False, True])
    print(res)
