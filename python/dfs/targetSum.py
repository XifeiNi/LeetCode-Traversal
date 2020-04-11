class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        return self.dfs(0, nums, 0, memo, S)
    def dfs(self, start, nums, curSum, memo, target):
        if (start, curSum) in memo:
            return memo[(start, curSum)]
        
        if start == len(nums):
            if curSum == target:
                return 1
            return 0
        
        ways = 0
        ways += self.dfs(start + 1, nums, curSum + nums[start], memo, target)
        ways += self.dfs(start + 1, nums, curSum - nums[start], memo, target)
        memo[(start, curSum)] = ways
        return ways
