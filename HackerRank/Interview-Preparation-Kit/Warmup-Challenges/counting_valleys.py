#!/bin/python3


# Complete the countingValleys function below.
def countingValleys1(n, s):
    height = 0
    prev_height = 0
    cnt = 0
    for i, element in enumerate(s):
        if element == 'U':
            height += 1
        elif element == 'D':
            height -= 1
        if height == 0 and prev_height < 0:
            cnt += 1
        prev_height = height
    return cnt


def countingValleys2(steps, path):
    level, count = 0, 0
    for step in path:
        if step == "D":
            level -= 1
        else:
            level += 1
            if level == 0:
                count += 1
    return count


if __name__ == '__main__':
    result = countingValleys1(8, "DDUUUUDD")
    print(result)

    result = countingValleys2(8, "UDDDUDUU")
    print(result)
