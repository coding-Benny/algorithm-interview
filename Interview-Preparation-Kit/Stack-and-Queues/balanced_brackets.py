#!/bin/python3

import os


# Complete the isBalanced function below.
def isBalanced(s):
    table = {')': '(', ']': '[', '}': '{'}

    for _ in range(len(s)):
        stack = []
        for bracket in s:
            if stack and table.get(bracket) == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        return "NO" if stack else "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result + '\n')
        fptr.write(result + '\n')

    fptr.close()
