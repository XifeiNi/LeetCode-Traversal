class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        n, m = len(A), len(B)
        f = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                if A[i] == B[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
        return f[n][m]
