# https://leetcode.com/problems/largest-number/
from typing import List


class Solution:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        i = 1

        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(''.join(map(str, nums))) if nums[0] != 0 else '0'


def main():
    solution = Solution()
    print(solution.largestNumber([10, 2]))  # "210"
    print(solution.largestNumber([3, 30, 34, 5, 9]))  # "954330"
    print(solution.largestNumber([1]))  # "1"
    print(solution.largestNumber([10]))  # "10"


if __name__ == '__main__':
    main()
