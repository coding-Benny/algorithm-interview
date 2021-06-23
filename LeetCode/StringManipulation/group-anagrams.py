from collections import defaultdict
from typing import List


def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    anagrams = []
    group = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        group[key].append(word)

    for key in group.keys():
        anagrams.append(group[key])

    return anagrams


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())


if __name__ == '__main__':
    res = groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
    res = groupAnagrams2([""])
    print(res)
    res = groupAnagrams2(["a"])
    print(res)
