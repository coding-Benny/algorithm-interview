#!/bin/python3


# Complete the alternatingCharacters function below.
def alternatingCharacters1(s):
    deletion = 0
    str = list(s)
    for idx in range(len(str)-1):
        if str[idx] == str[idx+1]:
            deletion += 1
    return deletion


def alternatingCharacters2(s):
    deletion = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            deletion += 1
    return deletion


if __name__ == '__main__':
    result = alternatingCharacters1("AAAA")
    print(result)

    result = alternatingCharacters1("BBBBB")
    print(result)

    result = alternatingCharacters2("ABABABAB")
    print(result)

    result = alternatingCharacters2("BABABA")
    print(result)

    result = alternatingCharacters2("AAABBB")
    print(result)
