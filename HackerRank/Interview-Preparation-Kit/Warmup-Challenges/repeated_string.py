#!/bin/python3


# Complete the repeatedString function below.
def repeatedString1(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


def repeatedString2(s, n):
    times = n // len(s)
    remains = n % len(s)

    if s in "a":
        return times

    count_a_in_s, count_a_in_remains = Counter(s).get("a"), Counter(s[:remains]).get("a")
    if not count_a_in_s:
        return 0
    if not count_a_in_remains:
        count_a_in_remains = 0

    count = count_a_in_s * times + count_a_in_remains if remains else count_a_in_s * times
    return count


if __name__ == '__main__':
    result = repeatedString1("aba", 10)
    print(result)

    result = repeatedString1("a", 1000000000000)
    print(result)

    result = repeatedString2("ceebbcb", 817723)
    print(result)

    result = repeatedString2("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm", 736778906400)
    print(result)
