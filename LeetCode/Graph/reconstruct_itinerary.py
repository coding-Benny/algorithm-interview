# https://leetcode.com/problems/reconstruct-itinerary/
from typing import List
from collections import defaultdict


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)

    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs("JFK")

    # 다시 뒤접어 어휘 순 결과로
    return route[::-1]


def findItinerary2(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)

    # 그래프 순서대로 구성
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs("JFK")

    # 다시 뒤접어 어휘 순 결과로
    return route[::-1]


def findItinerary3(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)

    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']

    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    # 다시 뒤접어 어휘 순 결과로
    return route[::-1]


def main():
    print(findItinerary(
        [
            ["MUC", "LHR"], ["JFK", "MUC"],
            ["SFO", "SJC"], ["LHR", "SFO"]
        ]
    ))  # ["JFK","MUC","LHR","SFO","SJC"]
    print(findItinerary2(
        [
            ["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
            ["ATL", "JFK"], ["ATL", "SFO"]
        ]
    ))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
    print(findItinerary3(
        [
            ["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]
        ]
    ))  # ["JFK","NRT","JFK","KUL"]


if __name__ == '__main__':
    main()
