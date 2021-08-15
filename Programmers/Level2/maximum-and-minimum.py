# https://programmers.co.kr/learn/courses/30/lessons/12939

# my solution
def solution(s):
    nums = list(map(int, s.split()))
    return "{} {}".format(min(nums), max(nums))


def main():
    print(solution("1 2 3 4"))  # "1 4"
    print(solution("-1 -2 -3 -4"))  # "-4 -1"
    print(solution("-1 -1"))  # "-1 -1"


if __name__ == '__main__':
    main()
