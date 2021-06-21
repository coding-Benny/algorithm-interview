def reorderLogFiles1(logs: list) -> list:
    letters, digits = [], []
    for log in logs:
        log_list = log.split()
        if log_list[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
            letters.sort(key=lambda letter: (letter.split()[1:]))
    return letters + digits


def reorderLogFiles2(logs: list) -> list:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda letter: (letter.split()[1:]))
    return letters + digits


if __name__ == '__main__':
    res = reorderLogFiles1(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
    print(res)
    res = reorderLogFiles2(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"])
    print(res)
