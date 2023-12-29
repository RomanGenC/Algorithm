class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # First solution
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

        # Second solution

        # nums[:] = sorted(set(nums))
        # return len(nums)