from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = {}
        for num in nums:
            result.setdefault(num, 0)
            result[num] += 1

            if result[num] == 2:
                del result[num]

        return list(result)[0]