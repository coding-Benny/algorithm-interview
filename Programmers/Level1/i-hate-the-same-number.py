# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr: list) -> list:
    left = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            left.append(arr[i])
    return left


if __name__ == '__main__':
    res = solution([1, 1, 3, 3, 0, 1, 1])
    print(res)
    res = solution([4, 4, 4, 3, 3])
    print(res)
