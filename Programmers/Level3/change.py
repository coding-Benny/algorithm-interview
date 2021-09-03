# https://programmers.co.kr/learn/courses/30/lessons/12907


# my solution - passes only the accuracy test, not the efficiency test(70.0/100.0)
def solution(n, money):
    cases = []

    def dfs(csum, index, case):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            cases.append(case)
            return

        for i in range(index, len(money)):
            dfs(csum - money[i], i, case + [money[i]])

    dfs(n, 0, [])

    return len(cases)


def main():
    print(solution(5, [1, 2, 5]))  # 4


if __name__ == '__main__':
    main()
