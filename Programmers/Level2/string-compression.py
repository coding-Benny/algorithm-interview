# https://programmers.co.kr/learn/courses/30/lessons/60057


# my solution
def solution(s):
    unit, compressed = 1, []

    while unit <= len(s) // 2 + 1:
        count, slices = 1, []

        for i in range(0, len(s) - unit + 1, unit):
            if s[i:i + unit] == s[i + unit:i + 2 * unit]:
                count += 1
            else:
                slices.append(str(count) + s[i:i + unit] if count > 1 else s[i:i + unit])
                count = 1
        else:
            # for 문을 다 돌고도 남은 문자열이 있으면 리스트에 추가
            if s[i + unit:]:
                slices.append(s[i + unit:])

        if slices:
            compressed.append(''.join(slices))
        unit += 1

    return len(sorted(compressed, key=len)[0])


# another solution
def compress(text, tok_len):
    words = [text[i:i + tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution2(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])


def main():
    print(solution("aabbaccc"))  # 7 (2a2ba3c)
    print(solution("ababcdcdababcdcd"))  # 9 (2ababcdcd)
    print(solution("abcabcdede"))  # 8 (2abcdede)
    print(solution("abcabcabcabcdededededede"))  # 14 (2abcabc2dedede)
    print(solution("xababcdcdababcdcd"))  # 17 (xababcdcdababcdcd)
    print(solution2("ababcdcdababcdcdx"))  # 10 (2ababcdcdx)
    print(solution2("aababa"))  # 5 (aa2ba)
    print(solution2("aaaaaaaaaa"))  # 3 (10a)
    print(solution2("aaaaaaaaaaaaaaabbbbbbbbbbc"))  # 7 (15a10bc)


if __name__ == '__main__':
    main()
