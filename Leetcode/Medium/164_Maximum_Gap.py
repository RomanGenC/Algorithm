class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i + 1] - nums[i] > m:
                m = nums[i + 1] - nums[i]
        return m