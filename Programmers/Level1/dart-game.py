# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult: str) -> int:
    score = []
    for i, result in enumerate(dartResult):
        if result.isdigit():
            if dartResult[i - 1].isdigit():
                score.append(score.pop() * 10 + int(result))
            else:
                score.append(int(result))
        elif result.isupper():
            if result == 'D':
                score.append(score.pop() ** 2)
            elif result == 'T':
                score.append(score.pop() ** 3)
        else:
            if result == '*':
                if len(score) == 1:
                    score.append(score.pop() * 2)
                else:
                    score.append(score.pop() * 2)
                    score.insert(-2, score.pop(-2) * 2)
            else:
                score.append(score.pop() * -1)
    return sum(score)


if __name__ == '__main__':
    res = solution("1S2D*3T")
    print(res)

    res = solution("1D2S#10S")
    print(res)

    res = solution("1D2S0T")
    print(res)

    res = solution("1S*2T*3S")
    print(res)

    res = solution("1D#2S*3S")
    print(res)

    res = solution("1T2D3D#")
    print(res)

    res = solution("1D2S3T*")
    print(res)