class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        result = ''
        for i in b:
            result += str(i)
        return pow(a, int(result), 1337)