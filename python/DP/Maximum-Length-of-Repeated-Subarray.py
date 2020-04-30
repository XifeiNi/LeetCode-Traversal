class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
        ret = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                ret = max(ret, dp[i][j])
        return ret
        
