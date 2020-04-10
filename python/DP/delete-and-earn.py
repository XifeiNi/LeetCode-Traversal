from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0 for _ in range(20001)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        dp[1] = count[1]
        for i in range(2, 20001):
            dp[i] = max(dp[i - 1], dp[i - 2] + count[i] * i)
        return dp[20000]
