# https://programmers.co.kr/learn/courses/30/lessons/42579
from collections import defaultdict


# my solution
def solution(genres, plays):
    album_table = defaultdict(list)
    best_albums = []

    for no, genre in enumerate(genres):
        album_table[genre].append((no, plays[no]))

    for genre in album_table:
        album_table[genre].sort(key=lambda music: music[1], reverse=True)

    for genre in sorted(list(album_table.values()),
                        key=lambda albums: sum([album[1] for album in albums]), reverse=True):
        for m in genre[:2]:
            best_albums.append(m[0])

    return best_albums


# another solution
def solution2(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer


def main():
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
    print(solution2(["classic", "pop", "classic", "classic", "classic"], [500, 1000, 400, 300, 200, 100]))  # [0, 2, 1]


if __name__ == '__main__':
    main()
