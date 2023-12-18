class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(i for i in nums1)
        set2 = set(i for i in nums2)

        ans1 = list(i for i in (set1 - set2))
        ans2 = list(i for i in (set2 - set1))

        print(ans1 , ans2)
        return [ans1 , ans2]

