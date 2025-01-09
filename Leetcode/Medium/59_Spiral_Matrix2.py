from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        directions = ['right', 'down', 'left', 'top']
        counter = route = i = j = 0
        direction_by_nums = {
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1],
            'top': [-1, 0],
        }
        while counter < n * n:
            counter += 1
            matrix[i][j] = counter
            temp_i = i + direction_by_nums[directions[route % 4]][0]
            temp_j = j + direction_by_nums[directions[route % 4]][1]
            if not (0 <= temp_i <= n - 1 and 0 <= temp_j <= n - 1 and matrix[temp_i][temp_j] == 0):
                route += 1

            i += direction_by_nums[directions[route % 4]][0]
            j += direction_by_nums[directions[route % 4]][1]

        return matrix
