# https://programmers.co.kr/learn/courses/30/lessons/76502


# my solution
def solution(s):
    table = {
        ')': '(', '}': '{', ']': '['
    }
    count, stack = 0, []

    for i in range(len(s)):
        rotated = s[i:] + s[:i]

        for parenthesis in rotated:
            if parenthesis in table:
                if stack and table.get(parenthesis) == stack[-1]:
                    stack.pop()
                else:
                    break
            else:
                stack.append(parenthesis)
        else:
            if not stack:
                count += 1

    return count


def main():
    print(solution("[](){}"))  # 3
    print(solution("}]()[{"))  # 2
    print(solution("[)(]"))  # 0
    print(solution("}}}"))  # 0


if __name__ == '__main__':
    main()
