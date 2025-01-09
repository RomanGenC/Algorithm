from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        directions = ['right', 'down', 'left', 'top']
        result = []
        counter = route = i = j = 0
        direction_by_nums = {
            'right': [0, 1],
            'down': [1, 0],
            'left': [0, -1],
            'top': [-1, 0],
        }
        while counter < n * m:
            counter += 1
            result.append(matrix[i][j])
            matrix[i][j] = 'X'
            temp_i = i + direction_by_nums[directions[route % 4]][0]
            temp_j = j + direction_by_nums[directions[route % 4]][1]
            if not (0 <= temp_i <= n - 1 and 0 <= temp_j <= m - 1 and matrix[temp_i][temp_j] != 'X'):
                route += 1

            i += direction_by_nums[directions[route % 4]][0]
            j += direction_by_nums[directions[route % 4]][1]

        return result
