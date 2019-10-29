class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(nums, 0, [], results)
        return results
    def dfs(self, nums, index, currentSub, results):
        results.append(list(currentSub))
        for i in range(index, len(nums)):
            currentSub.append(nums[i])
            self.dfs(nums, i+1, currentSub, results)
            currentSub.pop()
        
            
