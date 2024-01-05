class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_size = 0 # 出現0的區間
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_size += 1
            # 遇到非0
            else:
                # 和0區間的第一個0交換
                temp = nums[i]
                nums[i] = 0
                nums[i - zero_size] = temp
            