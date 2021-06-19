import re
from collections import deque


def isPalindrome1(s: str):
    s = re.sub('[^0-9a-zA-Z]', '', s).lower()
    return s == s[::-1]


def isPalindrome2(s: str):
    chars = []
    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    while len(chars) < 1:
        if chars.pop(0) != chars.pop():
            return False
    return True


def isPalindrome3(s: str):
    chars = deque()

    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    while len(chars) < 1:
        if chars.popleft() != chars.pop():
            return False
    return True


if __name__ == '__main__':
    res1 = isPalindrome1('A man, a plan, a canal: Panama')
    print(res1)
    res2 = isPalindrome2('race a car')
    print(res2)
    res3 = isPalindrome3('a_ba')
    print(res3)
