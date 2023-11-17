class Solution:
    def mySqrt(self, x: int) -> int:
        
        lo = 1
        hi = x
        
        while lo <= hi:
            mid = (lo + hi) // 2
            power = mid * mid
            if power == x:
                return mid
            elif power > x:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi