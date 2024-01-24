class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # FIRST SOLUTION
        if n <= 0:
            return False
        import math
        e = math.log(n, 3)
        return abs(e - round(e)) < 1e-10

        #SECOND SOLUTION
        temp = 1
        while temp <= n:
            if temp == n:
                return True
            temp *= 3
        return False