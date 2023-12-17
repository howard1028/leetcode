class Solution:
    def arraySign(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        zero = 0
        for i in nums:
            if i > 0:
                pos += 1
            elif i < 0:
                neg += 1
            else:
                zero += 1
        if zero > 0:
            return 0
        else:
            if neg % 2 == 0:
                return 1
            else:
                return -1