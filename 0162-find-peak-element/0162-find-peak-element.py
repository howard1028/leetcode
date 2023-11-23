class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 檢查長度1
        if n == 1:
            return 0
        
        # 檢查頭尾
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1

        # 檢查中間
        lo = 1
        hi = n - 2

        while lo <= hi:
            mid = lo +(hi - lo) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            # 左小右大
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            # 左大右小
            elif nums[mid] < nums[mid - 1]:
                hi = mid - 1
        return lo