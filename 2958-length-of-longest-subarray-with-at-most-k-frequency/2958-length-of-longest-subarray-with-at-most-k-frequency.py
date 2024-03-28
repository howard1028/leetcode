class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    
        t = defaultdict(int) # 出現次數
        curr = 0 # 目前subarray長度
        
        left = 0
        for right in range(len(nums)):
            t[nums[right]] += 1
            while t[nums[right]] > k:
                t[nums[left]] -= 1
                left += 1
            curr = max(right - left + 1 , curr)
        return curr