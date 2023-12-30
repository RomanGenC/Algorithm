class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # FIRST SOLUTION
        return nums.index(max(nums))

        # SECOND SOLUTION
        digits = {}
        counter = 0
        m = -10000000000
        for i in nums:
            if i > m:
                m = i
            digits[i] = counter
            counter += 1
        return digits[m]