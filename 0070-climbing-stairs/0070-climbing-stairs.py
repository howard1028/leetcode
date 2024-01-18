class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[1] = 1
        dp[2] = 2

        # 上一步走一步到現在
        # 上上步走兩步到現在
        for i in range(3,46):
            dp[i] = dp[i-1] + dp[i-2] 
        return dp[n]