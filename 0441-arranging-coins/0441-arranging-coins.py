import math

class Solution:
    def arrangeCoins(self, n: int) -> int:

        # 找高(row)

        # 1 2 : 1 row
        # 3 4 5 : 2 row
        # 6 7 8 9 : 3 row
        # 10 11 12 13 14 : 4 row

        lo = 1
        # hi = math.ceil(math.sqrt(n))
        hi = n

        # 最後一個高度也要檢查
        while lo <= hi:
            mid = (lo + hi) // 2
            # mid高的金幣數量
            total = ((1 + mid) * mid) // 2

            if total == n:
                return mid
            # 如果目前高度的金幣數量比n小，則高度應該更高
            elif total < n:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
            
        