class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2
            # 正常index是奇數的和前面那項會是同樣數字
            if mid % 2 == 1: # 用出現第一次的當index
                mid -= 1

            if nums[mid] != nums[mid + 1]: # 和後面的不同，則一個的在前面
                hi = mid
            else:
                lo = mid + 2
        return nums[lo]


