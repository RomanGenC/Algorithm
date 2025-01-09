# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left + 1 < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
                continue

            left = middle

        return right