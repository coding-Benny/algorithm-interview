# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers: list) -> list:
    add = []
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers)):
            if i != j:
                add.append(numbers[i] + numbers[j])
    return sorted(list(set(add)))


if __name__ == '__main__':
    res = solution([2, 1, 3, 4, 1])
    print(res)
    res = solution([5, 0, 2, 7])
    print(res)
