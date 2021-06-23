import re
from typing import List
from collections import Counter


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]+', ' ', paragraph).lower().split()
             if word not in banned]
    count = Counter(words)
    return count.most_common(1)[0][0]


if __name__ == '__main__':
    res = mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(res)
    res = mostCommonWord("a.", [])
    print(res)
