from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]

        # Second Solution

        range_len = len(nums)
        for i in range(range_len):
            if i == range_len - 1:
                return nums[0]

            if nums[i] > nums[i + 1]:
                return nums[i + 1]
