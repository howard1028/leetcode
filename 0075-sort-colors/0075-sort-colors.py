class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 荷蘭國旗問題

        left = 0
        current = 0
        right = len(nums) - 1

        print(current,right)
        while current <= right:
            if nums[current] == 0:

                temp = nums[left]
                nums[left] = nums[current]
                nums[current] = temp

                left += 1
                current += 1

            elif nums[current] == 1:
                current += 1

            elif nums[current] == 2:
                temp = nums[current]
                nums[current] = nums[right]
                nums[right] = temp

                right -= 1

            print(left,current,right)
            print(nums)