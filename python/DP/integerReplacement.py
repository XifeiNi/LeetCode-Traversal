class Solution:
    def integerReplacement(self, n: int) -> int:
        
        dp = {}    
        def solve(n):
            if n in dp:
                return dp[n]
            if n == 1:
                res =  0
            elif n % 2:
                res = min(solve(n + 1), solve(n - 1)) + 1 
            else:
                res =  solve(n // 2) + 1
            dp[n] = res
            return res
        return solve(n)
