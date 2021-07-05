def solution(arr: list) -> list:
    arr.remove(min(arr))
    if not arr:
        arr.append(-1)
    return arr


if __name__ == '__main__':
    res = solution([4, 3, 2, 1])
    print(res)
    res = solution([10])
    print(res)
