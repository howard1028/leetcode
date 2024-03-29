class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]

        for j in range(1,len1+1,1):
            for i in range(1,len2+1,1):
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1] , dp[i-1][j])
        return dp[-1][-1]
