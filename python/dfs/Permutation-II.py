class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.dfs(results, [], set(), sorted(nums))
        return results
    def dfs(self, results, current, visited, nums):
        if len(current) == len(nums):
            results.append(current[:])
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            if i != 0 and nums[i] == nums[i - 1] and i - 1 in visited:
                continue
            visited.add(i)
            current.append(nums[i])
            self.dfs(results, current, visited, nums)
            visited.remove(i)
            current.pop()
        
