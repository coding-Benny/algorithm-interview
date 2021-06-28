def solution(d: list, budget: int) -> int:
    total, count = 0, 0
    d.sort()
    for team in d:
        if total + team <= budget:
            total += team
            count += 1
    return count


if __name__ == '__main__':
    res = solution([1, 3, 2, 5, 4], 9)
    print(res)
    res = solution([2, 2, 3, 3], 10)
    print(res)
