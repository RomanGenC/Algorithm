class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        lenght = len(citations)
        citations = sorted(citations)
        for i in range(lenght - 1, -1, -1):
            if citations[i] >= h + 1:
                h += 1
            else:
                break
        return h