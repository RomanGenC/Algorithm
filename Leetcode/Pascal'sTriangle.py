class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        nums = [0] * numRows
        for i in range(numRows):
            nums[i] = [0] * numRows
        nums[0][0] = 1
        for i in range(1, numRows):
            for j in range(numRows):
                if j <= i:
                    nums[i][j] = nums[i - 1][j] + nums[i - 1][j - 1]
        for i in nums:
            result.append(i)
        for i in range(len(result)):
            result[i] = result[i][0:i + 1]
        return result


class Solution_2:
    def getRow(self, rowIndex: int) -> list[int]:
        next = rowIndex + 1
        result = []
        nums = [0] * next
        for i in range(rowIndex + 1):
            nums[i] = [0] * next
        nums[0][0] = 1
        for i in range(1, next):
            for j in range(next):
                if j <= i:
                    nums[i][j] = nums[i - 1][j] + nums[i - 1][j - 1]
        for i in nums:
            result.append(i)
        return result[rowIndex]
