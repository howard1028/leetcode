
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # 找平方根
        lo = 1
        hi = num

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
                