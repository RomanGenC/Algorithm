class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1 + nums2
        result.sort()
        if len(result) % 2 == 0:
            first = result[len(result)//2]
            second = result[len(result)//2 - 1]
            return (first + second)/2
        else:
            return result[len(result)//2]