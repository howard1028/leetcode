class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preSum = [0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            self.preSum.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]
        

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         res = 0
#         for i in range(left , right+1 , 1):
#             res += self.nums[i]
#         return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)