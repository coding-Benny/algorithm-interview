# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for parenthesis in s:
        if parenthesis == '(':
            stack.append(parenthesis)
        else:
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()

    return len(stack) == 0


def main():
    print(solution("()()"))
    print(solution("(())()"))
    print(solution(")()("))
    print(solution("(()("))


if __name__ == '__main__':
    main()
