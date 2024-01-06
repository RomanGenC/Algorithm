class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #FIRST SOLUTION
        return ' '.join(reversed(s.split()))

        #SECOND SOLUTION
        a = ''
        s = s.split()
        for i in range(len(s) - 1, -1, -1):
            a += s[i] + ' '
        return a[:-1]