class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        minimum = float("inf")

        while low < high:
            mid = (low + high) // 2
            minimum = min(minimum , nums[mid])

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 

        return nums[low]
