class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dict = {}
        for i,num in enumerate(numbers):
            component = target - num
            if component in dict:
                return [dict[component],i+1]
            else:
                dict[num] = i+1