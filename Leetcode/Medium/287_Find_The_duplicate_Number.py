from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        digits_map = {}
        for num in nums:
            if digits_map.get(num):
                return num

            digits_map[num] = 1
