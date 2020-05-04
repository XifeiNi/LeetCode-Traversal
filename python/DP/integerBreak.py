class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (1 + n)
        for i in range(1, 1 + n):
            dp[i] = i
            if i == n:
                dp[i] = 0
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i - j] * j)
        return dp[n]      
