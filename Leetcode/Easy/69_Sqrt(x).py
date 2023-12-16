class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while(right >= left):
            mid = (left + right)//2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                right = mid -1
            else:
                left = mid + 1
        return right