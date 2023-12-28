class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)[::-1]
        if x[-1] == '-':
            x = '-' + x[:-1]
        x = int(x)
        if x > 2**31 - 1 or x < -2**31:
            return 0
        return x