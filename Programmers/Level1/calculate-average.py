# https://programmers.co.kr/learn/courses/30/lessons/12944

def solution(arr: list) -> float:
    return sum(arr) / len(arr)


if __name__ == '__main__':
    res = solution([1, 2, 3, 4])
    print(res)

    res = solution([5, 5])
    print(res)
