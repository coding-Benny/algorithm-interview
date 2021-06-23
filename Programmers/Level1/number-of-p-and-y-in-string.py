def solution(s: str) -> bool:
    if s.lower().count('p') != s.lower().count('y'):
        return False
    return True


if __name__ == '__main__':
    res = solution("pPoooyY")
    print(res)
    res = solution("Pyy")
    print(res)
