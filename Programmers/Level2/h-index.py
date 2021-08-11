# https://programmers.co.kr/learn/courses/30/lessons/42747
# my solution
def solution(citations):
    count, h = 0, []
    while count <= max(citations):
        c = [citation for citation in citations if count <= citation]
        if len(c) >= count:
            h.append(count)
        count += 1
    return max(h)


# another solution
def solution2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


# another solution
def solution3(citations):
    citations = sorted(citations)
    length = len(citations)
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    return 0


def main():
    print(solution([3, 0, 6, 1, 5]))  # 3
    print(solution([31, 66]))   # 2
    print(solution2([0, 0, 0]))  # 0
    print(solution2([0, 1, 1]))  # 1
    print(solution3([0, 1, 2]))  # 1


if __name__ == '__main__':
    main()
