def reverseString1(s: list) -> None:
    # Trick when space complexity is limited to O(1)
    s[:] = s[::-1]
    print(s)


def reverseString2(s: list) -> None:
    s.reverse()
    print(s)


def reverseString3(s: list) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    print(s)


if __name__ == '__main__':
    reverseString1(["h", "e", "l", "l", "o"])
    reverseString2(["H", "a", "n", "n", "a", "h"])
    reverseString3(["w", "o", "r", "l", "d"])
