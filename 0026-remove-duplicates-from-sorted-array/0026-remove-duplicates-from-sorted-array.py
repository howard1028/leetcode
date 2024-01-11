class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            # 找第一次出現的放到前面
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j
