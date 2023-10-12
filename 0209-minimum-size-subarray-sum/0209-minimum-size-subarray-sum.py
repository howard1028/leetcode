class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i = 0 #sliding window左邊界
        res = float("inf") #sliding window最小長度
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target: 
                res = min(res,j-i+1)
                sum -= nums[i]
                i+=1 #sliding window左邊界左移
        if res == float("inf"):
            return 0
        else :
            return res
                
        
        # nums.sort()
#         left = 0
#         while left <= len(nums):
#         while left <= len(nums)-1:
#             if right > len(nums)-1:
#                 break
#             temp = 0
#             for i in range(left,right,1):
#                 temp += nums[i]

#             print("temp=",temp)
#             if temp < target:
#                 right += 1
#             elif temp > target:
#                 left += 1
#             else:
#                 temp = right-left+1
#                 if temp < ans or ans == 0:
#                     ans = temp
#                 print(left,right)
#                 left += 1

        
#         return ans
                