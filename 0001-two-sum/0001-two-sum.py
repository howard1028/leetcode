class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #zip打包成tuple，轉成可修改的list
        num_index = list(zip(nums,range(len(nums)))) #[數1,0],[數1,1],...[數,index]
        num_index.sort() #照數字大小排
        left = 0
        right = len(num_index)-1
        
        while left<right:
            curr_sum = num_index[left][0]+num_index[right][0] #取數相加
            if curr_sum == target:
                return [num_index[left][1],num_index[right][1]] #取index
            elif curr_sum < target:
                left+=1
            else :
                right -=1