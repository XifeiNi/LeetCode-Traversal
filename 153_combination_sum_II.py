class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        num.sort()
        self.answer, combination, used = [], [], [0] * len(num)
        self.dfs(num, target, 0, 0, combination, used)
        return self.answer
    def dfs(self, nums, target, cur, currentSum, combination, used):
        if currentSum == target:
            self.answer.append(combination[:])
            return
        for i in range(cur, len(nums)):
            if currentSum + nums[i] <= target and (i == 0 or nums[i] != nums[i-1] or used[i-1] == 1): 
                combination.append(nums[i])
                used[i] = 1
                self.dfs(nums, target, i+1, currentSum + nums[i], combination, used)
                combination.pop()
                used[i] = 0
