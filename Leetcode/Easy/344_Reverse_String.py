class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #FIRST SOLUTION
        s.reverse()

        #SECOND SOLUTION
        s[:] = s[::-1]

        #THIRD SOLUTION
        begin, end = 0, len(s)-1
        while begin < end:
            s[begin],s[end] = s[end], s[begin]
            begin += 1
            end -= 1