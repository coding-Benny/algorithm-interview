# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


def solution2(number, k):
    st = []
    for i in range(len(number)):
        while st and k > 0 and st[-1] < number[i]:
            st.pop()
            k -= 1
        st.append(number[i])
    return ''.join(st[:len(st) - k])


def main():
    print(solution("1924", 2))  # 94
    print(solution2("1231234", 3))  # 3234
    print(solution("4177252841", 4))  # 775841


if __name__ == '__main__':
    main()
