from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        s = 0
        m = 0
        for i , num in enumerate(nums):
            if num == 1:
                s += 1
            else:
                s -= 1

            # 0、1個數相等
            if s == 0:
                m = i + 1
            # 不相等且之前出現過的case
            elif s in dic:
                m = max(m , i - dic[s])
            # 不相等且沒出現過的case
            else:
                dic[s] = i
        return m
