class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [1] * n
        
        #只看左邊
        before = 1
        for i in range(n):
            output[i] *= before
            before *= nums[i]
            
        #只看右邊
        after = 1
        for i in range(n-1,-1,-1):
            output[i] *= after
            after *= nums[i]
        
        return output