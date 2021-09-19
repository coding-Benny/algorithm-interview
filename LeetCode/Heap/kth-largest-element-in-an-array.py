# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heap = list()

    # 최소 힙만 지원하므로 음수로 저장
    for n in nums:
        heapq.heappush(heap, -n)

    # 최대 힙처럼 동작하도록 가장 낮은 수부터 추출
    for _ in range(1, k):
        heapq.heappop(heap)

    # k번째 큰 요소를 부호를 변환하여 리턴
    return -heapq.heappop(heap)


def findKthLargest2(nums: List[int], k: int) -> int:
    # heapify는 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산, 이후 값을 추가하면 특성 깨짐 유의
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)


def findKthLargest3(nums: List[int], k: int) -> int:
    # nlargest: k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴
    # nsmallest: k번째만큼 작은 값이 가장 작은 값부터 순서대로 리스트로 리턴
    return heapq.nlargest(k, nums)[-1]


def findKthLargest4(nums: List[int], k: int) -> int:
    # 추가, 삭제가 빈번할 때는 힙 정렬이 유용하지만, 입력값이 고정되어 있다면 정렬도 ok
    return sorted(nums, reverse=True)[k - 1]


def main():
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(findKthLargest2([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(findKthLargest3([3, 2, 1, 5, 6, 4], 2))  # 5
    print(findKthLargest4([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4


if __name__ == '__main__':
    main()
