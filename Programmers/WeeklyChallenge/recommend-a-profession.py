# https://programmers.co.kr/learn/courses/30/lessons/84325


# my solution
def solution(table, languages, preference):
    scores = []

    for profession in table:
        info = profession.split()
        score = sum([(5 - info[1:].index(language)) * preference[i]
                     for i, language in enumerate(languages) if language in info[1:]])
        scores.append((score, info[0]))

    return sorted(scores, key=lambda s: (-s[0], s[1]))[0][1]


# another solution
def solution2(table, languages, preference):
    score = {}
    for t in table:
        for lang, pref in zip(languages, preference):
            if lang in t.split():
                score[t.split()[0]] = score.get(t.split()[0], 0) + (6 - t.split().index(lang)) * pref
    return sorted(score.items(), key=lambda item: [-item[1], item[0]])[0][0]


def main():
    print(
        solution(
            [
                "SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"
            ],
            ["PYTHON", "C++", "SQL"],
            [7, 5, 5]
        )
    )  # "HARDWARE"
    print(
        solution2(
            [
                "SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                "GAME C++ C# JAVASCRIPT C JAVA"
            ],
            ["JAVA", "JAVASCRIPT"],
            [7, 5]
        )
    )  # "PORTAL"


if __name__ == '__main__':
    main()
