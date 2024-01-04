class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1的0是先幫nums2留的位子

        p1 = m - 1
        p2 = n - 1
        p = m + n - 1 # 合併後的指針

        print(p1,p2)

        while p1 >= 0 and p2 >= 0:
            print(p1,p2)
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 如果nums2還有剩，則剩比較小的，全部加到nums1前面
        nums1[:p2+1] = nums2[:p2+1]