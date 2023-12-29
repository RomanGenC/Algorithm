class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = sorted(nums1 + nums2)
        n = len(result)
        if n % 2 == 0:
            return (result[n//2] + result[n//2 - 1])/2
        return result[n//2]