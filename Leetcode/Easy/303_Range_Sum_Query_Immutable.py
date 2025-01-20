class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.summary = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.summary.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.summary[right]
        return self.summary[right] - self.summary[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
