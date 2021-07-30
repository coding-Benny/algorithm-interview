import bisect
from typing import List


def search1(nums: List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        return -1

    return binary_search(0, len(nums) - 1)


def search2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def search3(nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1


def search4(nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1


def main():
    print(search1([-1, 0, 3, 5, 9, 12], 9))
    print(search2([-1, 0, 3, 5, 9, 12], 2))
    print(search3([-1, 0, 3, 5, 9, 12], 9))
    print(search4([-1, 0, 3, 5, 9, 12], 2))


if __name__ == '__main__':
    main()
