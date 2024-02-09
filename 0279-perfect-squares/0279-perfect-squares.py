class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1) # dp[i]放i的最小完全平方數的數量和
        dp[0] = 0

        for i in range(1 , n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i] , dp[i - j*j] + 1) # 某數+某個完全平方數(+1)
                j += 1
            # print(dp)
        return dp[n]
