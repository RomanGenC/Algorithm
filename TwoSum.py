class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      ind = [0] * 2
      for i in range(len(nums)):
        for j in range(1, len(nums)):
            if i != j and target == nums[i] + nums[j]:
                ind[0] = i
                ind[1] = j
                return ind