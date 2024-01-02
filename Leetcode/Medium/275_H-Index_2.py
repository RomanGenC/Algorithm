class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        lenght = len(citations)
        left = 0
        right = lenght - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= lenght - mid:
                right = mid - 1
            else:
                left = mid + 1
        return lenght - left