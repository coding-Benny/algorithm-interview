# https://programmers.co.kr/learn/courses/30/lessons/49994

# my solution
def solution(dirs):
    old_x, old_y, new_x, new_y, count = 0, 0, 0, 0, 0
    paths = []
    for dir in dirs:
        if dir == 'U':
            if old_y + 1 <= 5:
                new_y = old_y + 1
            else:
                continue
        elif dir == 'D':
            if old_y - 1 >= -5:
                new_y = old_y - 1
            else:
                continue
        elif dir == 'L':
            if old_x - 1 >= -5:
                new_x = old_x - 1
            else:
                continue
        elif dir == 'R':
            if old_x + 1 <= 5:
                new_x = old_x + 1
            else:
                continue

        paths.append((old_x, old_y, new_x, new_y))
        old_x, old_y = new_x, new_y

    paths = list(set(paths))
    duplicates = [paths[i] for i in range(len(paths) - 1) for j in range(i + 1, len(paths))
                  if paths[i][0] == paths[j][2] and paths[i][1] == paths[j][3] and
                  paths[i][2] == paths[j][0] and paths[i][3] == paths[j][1]]
    visits = [visit for visit in paths if visit not in duplicates]

    return len(visits) if paths else 1


# another solution
def solution2(dirs):
    s = set()
    d = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s) // 2


def main():
    print(solution("ULURRDLLU"))  # 7
    print(solution("LULLLLLLU"))  # 7
    print(solution("UDUD"))  # 1
    print(solution("UDU"))  # 1
    print(solution2("LLLLRLRLRLL"))  # 5
    print(solution2("UUUUDUDUDUUU"))  # 5
    print(solution2("LRLRL"))  # 1
    print(solution2("RRLL"))  # 2


if __name__ == '__main__':
    main()
