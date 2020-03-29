class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[n for _ in range(len(arr))] for _ in range(len(arr))]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if l == r:
                    dp[l][r] = 1
                elif l + 1 == r:
                    dp[l][r] = 2
                    if arr[l] == arr[r]:
                        dp[l][r] = 1
                else:
                    dp[l][r] = min(
                        dp[l + 1][r - 1] + (0 if arr[l] == arr[r] else 2),
                        dp[l][r], dp[l + 1][r] + 1,
                        dp[l][r - 1] + 1)
                    for k in range(l, r):
                        dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])
        return dp[0][n - 1]
