class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        dp = [[sys.maxsize for _ in range(len(A))] for _ in range(2)]
        dp[0][0], dp[1][0] = 0, 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp[0][i] = min(dp[0][i], dp[0][i - 1])
                dp[1][i] = min(dp[1][i], dp[1][i - 1] + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                dp[0][i] = min(dp[0][i], dp[1][i - 1])
                dp[1][i] = min(dp[1][i], dp[0][i - 1] + 1)
        return min(dp[0][-1], dp[1][-1])
                                
                             
