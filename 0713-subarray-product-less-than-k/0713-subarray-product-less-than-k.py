class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        res = 0 # 乘積比k大的個數
        temp = 1 # 目前乘積

        left = 0
        for right in range(len(nums)):
            temp *= nums[right]
            while temp >= k:
                temp /= nums[left]
                left += 1
                # print(temp)
            res += right - left + 1
        return res