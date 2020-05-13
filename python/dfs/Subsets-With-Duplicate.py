class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(sorted(nums), 0, [], results)
        return results
    
    def dfs(self, nums, start, current, results):
        results.append(list(current))
        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue
            current.append(nums[i])
            self.dfs(nums, i + 1, current, results)
            current.pop()
