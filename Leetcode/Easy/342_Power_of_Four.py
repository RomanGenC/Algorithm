class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #FIRST SOLUTION
        if n <= 0:
            return False
        import math
        e = math.log(n, 4)
        return e.is_integer()

        #SECOND SOLUTION
        temp = 1
        while temp <= n:
            if temp == n:
                return True
            temp *= 4
        return False