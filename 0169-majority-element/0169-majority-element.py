from collections import Counter
import operator

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        # max(c.items() , key = lambda x:x[1]) return一組items(3,2)
        # return max(c.items() , key = lambda x:x[1])[0] 
                
        return max(c.items(), key=operator.itemgetter(1))[0]