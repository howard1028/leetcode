class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        majority_time = float("-inf") # 出現次數
        majority = 0 # 出現次數最多的數字

        print(count)
        for key , value in count.items(): # 要用.items()取出key-value鍵值對
            print(key , value)
            if value > majority_time:
                majority = key
                majority_time = value
    
        return majority