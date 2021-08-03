from collections import Counter
import string


def is_corrected(parenthesis):
    stack = []

    for bracket in parenthesis:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()

    return len(stack) == 0


def split_balanced_parenthesis(string):
    for i in range(2, len(string) + 1, 2):
        counter = Counter(string[:i])
        if counter.get('(') == counter.get(')'):
            return string[:i], string[i:]


def solution(p):
    string = ''
    if not p or is_corrected(p):
        return p

    u, v = split_balanced_parenthesis(p)

    if is_corrected(u):
        return u + solution(v)
    else:
        string += '('
        string += solution(v)
        string += ')'
        string += u[1:len(u) - 1].translate(string.maketrans("()", ")("))
        return string


def main():
    print(solution(""))
    print(solution("(()())()"))
    print(solution(")("))
    print(solution("()))((()"))  # "()(())()"


if __name__ == '__main__':
    main()
