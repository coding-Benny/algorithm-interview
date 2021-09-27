# https://programmers.co.kr/learn/courses/30/lessons/12981


# my solution
def solution(n, words):
    for i, word in enumerate(words):
        if word in words[:i] or (i >= 1 and words[i - 1][-1] != word[0]):
            return [i % n + 1, i // n + 1]
    return [0, 0]


def main():
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))  # [3, 3]
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))  # [0, 0]
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))  # [1, 3]


if __name__ == '__main__':
    main()
