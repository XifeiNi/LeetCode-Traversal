class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        self.dfs(nums, [], results)
        return results
        
    def dfs(self, nums, temp, results):
        if len(temp) == len(nums):
            results.append(temp[:])
            return
        for i in range(0, len(nums)):
            if nums[i] not in temp:
                temp.append(nums[i])
                self.dfs(nums, temp, results)
                temp.pop()
            
