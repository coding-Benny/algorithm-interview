# https://leetcode.com/problems/intersection-of-two-arrays/
import bisect
from typing import List, Set


def intersection1(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return list(result)


def intersection2(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()
    nums2.sort()

    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return list(result)


def intersection3(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()

    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()

    i = j = 0
    
    # 투 포인터 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return list(result)


def main():
    print(intersection1([1, 2, 2, 1], [2, 2]))  # [2]
    print(intersection2([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]
    print(intersection3([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]


if __name__ == '__main__':
    main()
