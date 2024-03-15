class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n # 從前面
        suffix = [1] * n # 從後面
        res = []

        for i in range(1 , n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2 , -1 , -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        # print(prefix , suffix)
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res