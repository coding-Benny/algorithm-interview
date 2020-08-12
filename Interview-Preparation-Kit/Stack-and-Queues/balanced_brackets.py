#!/bin/python3

import os


# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for bracket in s:
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.append(bracket)
        else:
            try:
                bracket_partner = stack.pop(-1)
                if bracket_partner == "(":
                    if bracket != ")":
                        return "NO"
                elif bracket_partner == "{":
                    if bracket != "}":
                        return "NO"
                elif bracket_partner == "[":
                    if bracket != "]":
                        return "NO"
            except IndexError:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result + '\n')
        fptr.write(result + '\n')

    fptr.close()
