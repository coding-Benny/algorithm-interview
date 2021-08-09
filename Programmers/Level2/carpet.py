# https://programmers.co.kr/learn/courses/30/lessons/42842
# my solution
def solution1(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = i
            h = yellow // w
            if w >= h:
                if (w + 2) * 2 + h * 2 == brown:
                    return [w + 2, h + 2]


# another solution
def solution2(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow // i + 2, i + 2]


def main():
    print(solution1(10, 2))   # [4, 3]
    print(solution1(8, 1))    # [3, 3]
    print(solution2(24, 24))  # [8, 6]
    print(solution2(50, 22))  # [24, 3]


if __name__ == '__main__':
    main()
