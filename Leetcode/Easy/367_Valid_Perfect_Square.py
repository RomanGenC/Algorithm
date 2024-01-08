class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #FIRST SOLUTION
        mid = 0
        counter = 1
        while mid <= num:
            mid = counter * counter
            if mid == num:
                return True
            counter += 1
        return False

        #SECOND SOLUTION
        result = num ** 0.5
        if int(result) == result:
            return True
        return False