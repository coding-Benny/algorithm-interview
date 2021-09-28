# https://programmers.co.kr/learn/courses/30/lessons/77484


# my solution
def solution(lottos, win_nums):
    table = {
        6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6
    }
    count = lottos.count(0)
    correct = [lotto for lotto in lottos if lotto in win_nums]

    if correct == lottos:
        return [1, 1]
    elif count == 6:
        return [1, 6]
    else:
        lowest, highest = len(correct), len(correct) + count
        return [table.get(highest), table.get(lowest)]


# another solution
def solution2(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return [rank[cnt_0 + ans], rank[ans]]


# another solution
def solution3(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]


def main():
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
    print(solution2([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
    print(solution3([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
    print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))  # [6, 6]


if __name__ == '__main__':
    main()
