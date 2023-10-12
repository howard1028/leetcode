class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicate = False
        num_dict = {}
        
        for i in range(len(nums)):
            if (num_dict.get(nums[i])):
                duplicate = True
            else:
                num_dict[nums[i]] = 1
                
        return duplicate