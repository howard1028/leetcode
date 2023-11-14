def findMin(nums,lo,hi):

    while lo < hi:
        mid = (lo + hi) // 2

        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return lo # 回傳min的index

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        lo = 0
        hi = len(nums) - 1
        min_index = findMin(nums,lo,hi)

        print(min_index)

        # 找右邊
        l = min_index
        h = len(nums) - 1
        
        while l < h:
            mid = (l+h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid
            else:
                l = mid + 1

        if nums[l] == target:
            return l

        # 找左邊
        l = 0
        h = min_index

        while l < h:
            mid = (l+h) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                h = mid
            else:
                l = mid + 1
                
        if nums[l] == target:
            return l

        return -1


            
