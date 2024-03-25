from collections import Counter
import heapq
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []

        for key , value in c.items():
            if value == 2:
                res.append(key)

        return res

