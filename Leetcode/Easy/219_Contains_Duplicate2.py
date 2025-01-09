from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_by_position = {}

        for pos, num in enumerate(nums):
            last_pos = num_by_position.get(num)
            if last_pos is not None and abs(last_pos - pos) <= k:
                return True

            num_by_position[num] = pos

        return False
