class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = len(nums1)- 1
        j = len(nums2) - 1

        res = -1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                j -= 1
            elif nums1[i] > nums2[j]:
                i -= 1
            else:
                res = nums1[i]
                i -= 1
                j -= 1
        return res