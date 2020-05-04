class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        dp = [[0 for _ in range(len(A))] for _ in range(len(A))]
        ret = 0
        for i in range(2, len(A)):
            left, right = 0, i - 1
            while left < right:
                twoSum = A[left] + A[right]
                if twoSum > A[i]:
                    right -= 1
                elif twoSum < A[i]:
                    left += 1
                else:
                    dp[right][i] = dp[left][right] + 1
                    ret = max(ret, dp[right][i])
                    right -= 1
                    left += 1
        if ret == 0:
            return ret
        return ret + 2
