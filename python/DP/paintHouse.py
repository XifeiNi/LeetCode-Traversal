class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        dp = [[float('inf')] * 3 for _ in costs]
        for i, cost in enumerate(costs):
            if i == 0:
                dp[0] = cost[:]
                continue
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[2]
        return min(dp[-1])
            
