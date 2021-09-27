# https://programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    width, height = max([s[0] for s in sizes]), max([s[1] for s in sizes])
    return width * height


def main():
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133


if __name__ == '__main__':
    main()
