class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or N >= K + W:
            return 1.0
        dp = [1.0] + [0.0] * N
        Wsum = 1.0
        for i in range(1, len(dp)):
            dp[i] = Wsum / W
            if i < K: 
                Wsum += dp[i]
            if i - W >= 0: 
                Wsum -= dp[i - W]
        return sum(dp[K:])
            
