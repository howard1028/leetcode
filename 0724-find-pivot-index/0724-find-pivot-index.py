class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_total = 0
        right_total = 0
        for num in nums:
            right_total += num

        for i in range(len(nums)):

            right_total -= nums[i]
            if i != 0:
                left_total += nums[i-1]

            print(left_total , right_total)
            if left_total == right_total:
                return i

        return -1