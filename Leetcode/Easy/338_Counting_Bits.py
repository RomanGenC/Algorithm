class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        #FIRST  SOLUTION
        result = []
        for i in range(n + 1):
            result.append(bin(i)[2:].count('1'))
        return result

        #SECOND  SOLUTION
        result = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                result.append(result[i // 2] + 1)
            else:
                result.append(result[i // 2])
        return result