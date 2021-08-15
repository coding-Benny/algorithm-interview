# https://programmers.co.kr/learn/courses/30/lessons/12951
import re


# my solution
def solution(s):
    words = re.split(r'(\s+)', s.lower())
    words = [word[0].upper() + word[1:] for word in words if len(word) > 0]

    return ''.join(words)


def main():
    print(solution("3people unFollowed me"))
    print(solution("for the last week"))
    print(solution("hello my     friend"))
    print(solution(" Starbucks Iced Americano "))


if __name__ == '__main__':
    main()