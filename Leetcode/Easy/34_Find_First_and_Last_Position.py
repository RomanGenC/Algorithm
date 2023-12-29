class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        n = len(nums)
        left = 0
        right = n - 1
        for i in range(0, n):
            if nums[left] == nums[right]:
                return [left, right]
            elif nums[left] < target:
                left += 1
            else:
                right -= 1