# https://programmers.co.kr/learn/courses/30/lessons/12924

# my solution
def solution(n):
    count = 0
    for i in range(1, n + 1):
        sum = 0
        for j in range(i, n + 1):
            sum += j
            if sum == n:
                count += 1
                break
            elif sum > n:
                break
    return count


# another solution
def solution2(n):
    return len([i for i in range(1, n + 1, 2) if n % i is 0])


def main():
    print(solution(15))


if __name__ == '__main__':
    main()
