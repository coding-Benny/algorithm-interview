# https://programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


# my solution
def solution(begin, target, words):
    # words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0

    # 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
    count = 0

    def dfs(current):
        nonlocal count
        count += 1
        diffs, next_words = [], []

        for word in words:
            diff = sum(current[i] != word[i] for i in range(len(current)))
            diffs.append(diff)

        for i, d in enumerate(diffs):
            if d == 1:
                next_words.append(words[i])

        if target in next_words:
            return
        else:
            next_word = words.pop(diffs.index(1))

        dfs(next_word)

    dfs(begin)
    return count


# another solution
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution2(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)


# another solution
def solution3(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x != y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1


def main():
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
    print(solution2("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
    print(solution2("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
    print(solution3("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
    print(solution3("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0


if __name__ == '__main__':
    main()
