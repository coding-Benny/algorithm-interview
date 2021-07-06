# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1: list, arr2: list) -> list:
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


if __name__ == '__main__':
    res = solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])
    print(res)

    res = solution([[1], [2]], [[3], [4]])
    print(res)
