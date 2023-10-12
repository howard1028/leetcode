class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            # 如果有重複則跳過
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    output.append([nums[i],nums[l],nums[r]])
                    # 找完後左邊指針往右移
                    l += 1
                    # 如果有重複則再往右移
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return output
                    