class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #FIRST SOLUTION
        nums[:] = nums.count(0) * [0] + nums.count(1) * [1] + nums.count(2) * [2]

        #SECOND SOLUTION
        dic = {0: 0, 1: 0, 2: 0}
        for i in nums:
            dic[i] += 1
        nums[:] = dic[0] * [0] + dic[1] * [1] + dic[2] * [2]