class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[i]) - 1
        while True:
            if target > matrix[i][j] and i < len(matrix) - 1:
                i += 1
            elif target < matrix[i][j] and j > 0:
                j -= 1
            elif target == matrix[i][j]:
                return True
            else:
                return False