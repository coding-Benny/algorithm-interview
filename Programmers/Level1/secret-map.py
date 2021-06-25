# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2) -> list:
    arr3 = []
    for i, elem in enumerate(arr1):
        arr1[i] = list(map(int, "{0:b}".format(elem).zfill(n)))

    for i, elem in enumerate(arr2):
        arr2[i] = list(map(int, "{0:b}".format(elem).zfill(n)))

    for i in range(n):
        tmp = []
        for j in range(n):
            if arr1[i][j] + arr2[i][j] >= 1:
                tmp.append('#')
            else:
                tmp.append(' ')
        arr3.append(''.join(tmp))
    return arr3


if __name__ == '__main__':
    res = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
    print(res)
    res = solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
    print(res)
