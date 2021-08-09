# https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque


# my solution
def solution1(prices):
    period = [0] * len(prices)
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            period[i] += 1
            if prices[i] > prices[j]:
                break
    return period


# another solution
def solution2(prices):
    period, prices = [], deque(prices)

    while prices:
        c = prices.popleft()
        count = 0

        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        period.append(count)
    return period


# another solution
def solution3(p):
    ans, stack = [0] * len(p), [0]

    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i - j
                    stack.remove(j)
                else:
                    break
        stack.append(i)

    for i in range(0, len(stack)-1):
        ans[stack[i]] = len(p) - stack[i] - 1

    return ans


def main():
    print(solution1([1, 2, 3, 2, 3]))
    print(solution2([1, 2, 3, 2, 3]))
    print(solution3([1, 2, 3, 2, 3]))


if __name__ == '__main__':
    main()
