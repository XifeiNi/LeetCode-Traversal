import sys
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [100000 for _ in range(n + 1)]
        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
        
