class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        index = int((left+right)/2)

        while (left<=right):
            index = int((left+right)/2)
            if target>nums[index]:
                left = index+1
                print(index)
            elif target<nums[index]:
                right = index-1
                print(index)
            elif target==nums[index]:
                return index
                print(index)
        return -1
            