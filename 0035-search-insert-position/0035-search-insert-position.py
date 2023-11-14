class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        # 長度 = 1        
        if low == high:
            if nums[0] == target or nums[0] > target:
                return 0
            else:
                return 1 

        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        # 最後判斷要插前面還後面
        if nums[low] >= target:
            return low
        else:
            return low + 1