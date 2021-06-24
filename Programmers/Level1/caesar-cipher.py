def solution(s: str, n: int) -> str:
    caesar = []
    for char in s:
        if char.isspace():
            caesar.append(char)
            continue
        if (char.islower() and ord(char) + n > ord('z')) or (char.isupper() and ord(char) + n > ord('Z')):
            caesar.append(chr(ord(char) + n - 26))
        else:
            caesar.append(chr(ord(char) + n))
    return ''.join(caesar)


if __name__ == '__main__':
    res = solution("AB", 1)
    print(res)
    res = solution("z", 1)
    print(res)
    res = solution("a B z", 4)
    print(res)
    res = solution("programmer", 3)  # surjudpphu
    print(res)
    res = solution("Kakao", 2)  # Mcmcq
    print(res)
    res = solution("NAVER", 25)  # MZUDQ
    print(res)