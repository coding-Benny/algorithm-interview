# https://programmers.co.kr/learn/courses/30/lessons/64061


# my solution
def solution(board, moves):
    basket = []
    count = 0
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move - 1]
            if doll != 0:
                if basket and doll == basket[-1]:
                    basket.pop()
                    count += 2
                else:
                    basket.append(doll)
                board[i][move - 1] = 0
                break
    return count


# another solution
def solution2(board, moves):
    stack_list = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stack_list.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stack_list) > 1:
                    if stack_list[-1] == stack_list[-2]:
                        stack_list.pop(-1)
                        stack_list.pop(-1)
                        answer += 2
                break

    return answer


def main():
    print(
        solution([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1]
        ],
            [1, 5, 3, 5, 1, 2, 1, 4]))  # 4
    print(
        solution2([
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1]
        ],
            [1, 5, 3, 5, 1, 2, 1, 4]))  # 4


if __name__ == '__main__':
    main()
