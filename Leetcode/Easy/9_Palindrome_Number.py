class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x = list(x)
        while len(x) >= 2:
            if x[0] != x[-1]:
                return False
            del x[0]
            del x[-1]
        return True

