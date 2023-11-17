class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x = list(x)
        while len(x) >= 2:
            if x[0] == x[-1]:
                del x[0]
                del x[-1]
            else:
                return False
        return True