class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            for j in range(i+1):
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1] == 1):
                    dp[j][i] = 1
                ans+=dp[j][i]
        return ans
