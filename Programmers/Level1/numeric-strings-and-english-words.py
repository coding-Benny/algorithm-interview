# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    word = ''
    result = []

    for c in s:
        if c.isdigit():
            result.append(c)
            continue
        else:
            word += c

        if word in dic:
            result.append(dic.get(word))
            word = ''
    return int(''.join(result))


if __name__ == '__main__':
    res = solution("one4seveneight")
    print(res)

    res = solution("23four5six7")
    print(res)

    res = solution("2three45sixseven")
    print(res)

    res = solution("123")
    print(res)