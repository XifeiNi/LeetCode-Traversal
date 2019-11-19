class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return len(s) == 0
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        maxLength = max([len(w) for w in wordDict])
        for i in range(1, n+1):
            for j in range(1, min(i, maxLength) + 1):
                if not dp[i - j]:
                    continue
                if s[i-j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
