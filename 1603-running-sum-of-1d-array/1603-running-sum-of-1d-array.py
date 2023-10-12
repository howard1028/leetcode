class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum2 = []
        for i in range(len(nums)):
            if i == 0:
                sum2.append(nums[i])
            else:
                sum2.append(nums[i]+sum2[i-1])
        return sum2