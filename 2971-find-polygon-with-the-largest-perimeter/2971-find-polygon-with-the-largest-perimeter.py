class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        p = 0 # 前面邊的和
        res = -1 # 最大周長

        for num in nums:
            # 兩邊和 > 第三邊：ok
            if p > num:
                res = p + num
            p += num
        return res
